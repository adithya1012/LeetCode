import heapq
from typing import List
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap = []
    for interval in intervals:
        start, end = interval
        if heap and heap[0] <= start:
            #### This is a if condition and not while. So you are not removing all the meeting which ended.
            #### You are removing only one and it will a set of meeting that were running continuously.
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)

print(minMeetingRooms([[1,2],[1,2],[2,3],[10,30]]))