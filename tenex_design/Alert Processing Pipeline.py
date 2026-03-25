import time
import heapq
from collections import defaultdict


# -------------------------------------------------------
# PHASE 1: Alert Model
# -------------------------------------------------------

class Alert:
    SEVERITY_RANK = {"critical": 1, "high": 2, "medium": 3, "low": 4}

    def __init__(self, alert_id, source, severity, message):
        self.alert_id = alert_id
        self.source = source
        self.severity = severity
        self.message = message
        self.timestamp = time.time()

    def fingerprint(self):
        """Dedup key — same source + message = same alert"""
        return f"{self.source}:{self.message}"

    def priority(self):
        return self.SEVERITY_RANK.get(self.severity, 99)

    # heapq needs this for comparison
    def __lt__(self, other):
        return self.priority() < other.priority()

    def __repr__(self):
        return f"[{self.severity.upper()}] ({self.source}) {self.message}"


# -------------------------------------------------------
# PHASE 2: Deduplication
# -------------------------------------------------------

class Deduplicator:
    def __init__(self, ttl_seconds=60):
        self.seen = {}  # fingerprint -> timestamp
        self.ttl = ttl_seconds

    def is_duplicate(self, alert):
        fp = alert.fingerprint()
        now = time.time()

        if fp in self.seen:
            if now - self.seen[fp] < self.ttl:
                return True  # still within TTL window, it's a dup

        self.seen[fp] = now  # first time or TTL expired, record it
        return False


# -------------------------------------------------------
# PHASE 3: Priority Queue (Ingestion Layer)
# -------------------------------------------------------

class AlertQueue:
    def __init__(self):
        self._heap = []

    def push(self, alert):
        heapq.heappush(self._heap, alert)

    def pop(self):
        if self._heap:
            return heapq.heappop(self._heap)
        return None

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)


# -------------------------------------------------------
# PHASE 4: Handlers
# -------------------------------------------------------

class Handler:
    def handle(self, alert):
        raise NotImplementedError


class AutoResolveHandler(Handler):
    def handle(self, alert):
        print(f"  ✅ AUTO-RESOLVED: {alert}")


class HumanEscalationHandler(Handler):
    def handle(self, alert):
        print(f"  🚨 ESCALATED TO HUMAN: {alert}")


class NotificationHandler(Handler):
    def handle(self, alert):
        print(f"  🔔 NOTIFICATION SENT: {alert}")


# -------------------------------------------------------
# PHASE 4: Router
# -------------------------------------------------------

class AlertRouter:
    def __init__(self):
        self.routes = {
            "critical": HumanEscalationHandler(),
            "high": HumanEscalationHandler(),
            "medium": NotificationHandler(),
            "low": AutoResolveHandler(),
        }
        self.default = AutoResolveHandler()

    def route(self, alert):
        handler = self.routes.get(alert.severity, self.default)
        handler.handle(alert)


# -------------------------------------------------------
# PHASE 4: Pipeline — ties it all together
# -------------------------------------------------------

class AlertPipeline:
    def __init__(self):
        self.deduplicator = Deduplicator(ttl_seconds=60)
        self.queue = AlertQueue()
        self.router = AlertRouter()
        self.stats = defaultdict(int)

    def ingest(self, alert):
        if self.deduplicator.is_duplicate(alert):
            print(f"  ⚠️  DUPLICATE DROPPED: {alert}")
            self.stats["duplicates"] += 1
            return

        self.queue.push(alert)
        self.stats["ingested"] += 1

    def process_all(self):
        print("\n--- Processing Alerts (highest priority first) ---")
        while not self.queue.is_empty():
            alert = self.queue.pop()
            self.router.route(alert)
            self.stats["processed"] += 1

    def print_stats(self):
        print(f"\n--- Stats ---")
        for k, v in self.stats.items():
            print(f"  {k}: {v}")


# -------------------------------------------------------
# DEMO
# -------------------------------------------------------

if __name__ == "__main__":
    pipeline = AlertPipeline()

    alerts = [
        Alert("a1", "firewall", "low", "Port scan detected"),
        Alert("a2", "firewall", "critical", "SSH brute force"),
        Alert("a3", "antivirus", "medium", "Suspicious file"),
        Alert("a4", "firewall", "low", "Port scan detected"),  # duplicate
        Alert("a5", "ids", "high", "SQL injection attempt"),
        Alert("a6", "ids", "high", "SQL injection attempt"),  # duplicate
        Alert("a7", "antivirus", "critical", "Ransomware signature"),
    ]

    print("--- Ingesting Alerts ---")
    for alert in alerts:
        pipeline.ingest(alert)

    pipeline.process_all()
    pipeline.print_stats()
