import heapq
from collections import Counter

test = ["B","C","D","A","A","A","A","G"]
count = Counter(test)
print(count)
heap = []
for key, val in count.items():
    heap.append([-val, 0])
heapq.heapify(heap)
val, t = heapq.heappop(heap)
print(val, t)