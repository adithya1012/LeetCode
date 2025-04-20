
from collections import Counter
import heapq
def leastInterval(tasks, n):
    vals = Counter(tasks)
    count = []
    for key, val in vals.items():
        count.append([-val, 1, key])
    heapq.heapify(count)
    time = 1
    while count:
        rem, time_a, c = heapq.heappop(count)
        if time < time_a:
            time = time_a
        if rem + 1 != 0:
            heapq.heappush(count, [rem + 1, time + n +1, c])
        time += 1
    return time

print(leastInterval(["A","A","A","B","B","B"], 3))