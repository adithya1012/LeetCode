# You're working at a restaurant with a single waitlist for party assignments. You need to implement the following operations:
from collections import defaultdict, deque


# AddWaitlist(partySize): Adds a party to the waitlist.
# RemoveWaitlist(partySize): Removes a party from the waitlist.
# FindParty(numSeats): Returns the earliest party from the waitlist whose size fits the given number of seats. Returns -1 if no suitable party is found.

from collections import defaultdict, deque


class Solution:
    def __init__(self, max_occupency):
        self.max_occupency = max_occupency
        self.time = 0
        self.waiting_counter = defaultdict(deque)

    def AddWaitlist(self, size):
        self.waiting_counter[size].append(self.time)
        self.time += 1

    def RemoveWaitlist(self, size):
        if self.waiting_counter[size]:  # ✅ Good to add this check
            self.waiting_counter[size].popleft()

    def FindParty(self, numSeats):
        min_time = float("inf")
        best_size = -1

        for i in range(1, min(numSeats, self.max_occupency) + 1):  # ✅ Cleaner
            if self.waiting_counter[i] and self.waiting_counter[i][0] < min_time:
                min_time = self.waiting_counter[i][0]  # ✅ Update min_time
                best_size = i

        if best_size != -1:
            self.waiting_counter[best_size].popleft()

        return best_size


sol = Solution(max_occupency=10)

sol.AddWaitlist(4)  # time=0
sol.AddWaitlist(2)  # time=1
sol.AddWaitlist(6)  # time=2
sol.AddWaitlist(3)  # time=3

print(sol.FindParty(5))  # Should return 2 (earliest party ≤5 is size 2 at time=1)
print(sol.FindParty(7))  # Should return 4 (earliest remaining party ≤7 is size 4 at time=0)
print(sol.FindParty(3))  # Should return 3 (size 3 at time=3)
print(sol.FindParty(10)) # Should return 6 (size 6 at time=2)
print(sol.FindParty(5))  # Should return -1 (no parties left)
