import heapq
from collections import defaultdict


def minimumTime(n: int, edges, disappear):
    graph = defaultdict(list)
    for u, v, l in edges:
        graph[u].append([v, l])
        graph[v].append([u, l])

    heap = [[0, 0, -1]]  # time, node, parent
    dist = [float("inf")] * n
    dist[0] = 0
    visit = set()

    while heap:
        time, node, parent = heapq.heappop(heap)
        # if disappear[node] <= time:
        #     continue
        # visit.add(node)
        for n, t in graph[node]:
            if n != parent:
                if dist[n] > t + time and t + time < disappear[n]:
                    dist[n] = t + time
                    heapq.heappush(heap, [t + time, n, node])
    for i in range(len(dist)):
        if dist[i] == float("inf"):
            dist[i] = -1
    return dist

print(minimumTime(n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]))
