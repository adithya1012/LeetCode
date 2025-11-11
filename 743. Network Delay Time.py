from collections import defaultdict
import heapq


def networkDelayTime(times, n: int, k: int) -> int:
    graph = defaultdict(list)
    for edge in times:
        graph[edge[0]].append([edge[2], edge[1]])

    if k not in graph:
        return -1
    print(graph)
    heap = graph[k].copy()
    heapq.heapify(heap)
    n -= 1
    visit = {k}
    print(heap)
    while heap:
        time, end = heapq.heappop(heap)
        n -= 1
        if not n:
            return time
        for edge in graph[end]:
            if edge[1] not in visit:
                visit.add(edge[1])
                heapq.heappush(heap, [time + edge[0], edge[0]])
    return -1

print(networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], n = 4, k = 1))