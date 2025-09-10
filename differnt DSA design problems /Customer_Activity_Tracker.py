# Problem Statement
# You're building a system for a CRM that needs to track and analyze customer interactions.
# The system receives a continuous stream of events (emails, calls, meetings, website visits) for different customers. You need to:
# Calculate real-time engagement scores based on interaction types and recency
# Identify "hot" prospects (customers with high recent activity)
# Provide fast lookups for customer activity history
# Handle time-based queries (activity in last 7 days, 30 days, etc.)
# Support bulk analytics queries across all customers

import heapq
import datetime

class Customer_Interaction:
    def __init__(self):
        self.heap = []
        self.customer = {}
        # {customerID:
            # { events: [
                # type :str
                # time: int ],
            # eng_score: int}
        # }
        self.event_weight = {"email":1, "phone":3, "meeting":5, "demo":10}

    def add_event(self, customerID, event_type, event_time):
        if customerID not in self.customer:
            self.customer[customerID] = {
                "events" : [],
                "score" : 0
            }

        self.customer[customerID]["event"].append({
            "type" : event_type,
            "time" : event_time
        })

        score = self._calculate_customer_score(customerID)
        self.customer[customerID]["score"] = score
        heapq.heappush(self.heap, (-score, customerID))

    def _calculate_customer_score(self, customerID):
        events = self.customer[customerID]["events"]
        score = 0
        for event in events:
            days = (datetime.datetime.now() - event["time"]).days
            dcaying_factor = 0.9 ** days
            score += self.event_weight.get(event["type"], 0) * dcaying_factor
        return score

    def top_k_hot_customers(self, k):
        tmp = []
        result = []
        while k:
            if self.heap:
                score, customerID = heapq.heappop(self.heap)
                result.append(customerID)
                tmp.append((score, customerID))
            else:
                break
        for score, customerID in tmp:
            heapq.heappush(self.heap, (score, customerID))
        return result





