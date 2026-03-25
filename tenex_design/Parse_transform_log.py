import csv
from dataclasses import dataclass
from datetime import datetime
from collections import defaultdict


# --- Data model ---

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    service: str
    message: str
    response_time_ms: int


# --- Step 1: Parse ---

def parse_log(filepath: str) -> list[LogEntry]:
    """Read CSV line by line and convert each row to a typed LogEntry."""
    entries = []
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                entry = LogEntry(
                    timestamp=datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S"),
                    level=row["level"].strip().upper(),
                    service=row["service"].strip(),
                    message=row["message"].strip(),
                    response_time_ms=int(row["response_time_ms"]),
                )
                entries.append(entry)
            except (ValueError, KeyError) as e:
                print(f"  Skipping bad row: {row} — {e}")
    return entries


# --- Step 2: Filter by level ---

def filter_by_level(entries: list[LogEntry], level: str) -> list[LogEntry]:
    """Return only entries matching the given log level."""
    return [e for e in entries if e.level == level.upper()]


# --- Step 3: Count errors per service ---

def errors_per_service(entries: list[LogEntry]) -> dict[str, int]:
    """Count ERROR entries grouped by service."""
    counts = defaultdict(int)
    for entry in entries:
        if entry.level == "ERROR":
            counts[entry.service] += 1
    return dict(counts)


# --- Step 4: Flag slow requests ---

def flag_slow_requests(entries: list[LogEntry], threshold_ms: int = 500) -> list[LogEntry]:
    """Return entries whose response time exceeds the threshold."""
    return [e for e in entries if e.response_time_ms > threshold_ms]


# --- Step 5: Summary report ---

def summarize(entries: list[LogEntry]) -> dict:
    """Produce a high-level summary of the log data."""
    if not entries:
        return {}

    level_counts = defaultdict(int)
    for e in entries:
        level_counts[e.level] += 1

    avg_response = sum(e.response_time_ms for e in entries) / len(entries)

    return {
        "total_entries": len(entries),
        "level_counts": dict(level_counts),
        "errors_per_service": errors_per_service(entries),
        "avg_response_time_ms": round(avg_response, 2),
        "slow_request_count": len(flag_slow_requests(entries)),
    }


# --- Main ---

if __name__ == "__main__":
    filepath = "logs.csv"

    print("=== Parsing logs ===")
    entries = parse_log(filepath)
    print(f"  Loaded {len(entries)} entries\n")

    print("=== Errors only ===")
    errors = filter_by_level(entries, "ERROR")
    for e in errors:
        print(f"  [{e.timestamp}] {e.service}: {e.message}")

    print("\n=== Errors per service ===")
    for service, count in errors_per_service(entries).items():
        print(f"  {service}: {count} error(s)")

    print("\n=== Slow requests (>500ms) ===")
    slow = flag_slow_requests(entries, threshold_ms=500)
    for e in slow:
        print(f"  [{e.service}] {e.response_time_ms}ms — {e.message}")

    print("\n=== Summary ===")
    report = summarize(entries)
    for key, value in report.items():
        print(f"  {key}: {value}")
