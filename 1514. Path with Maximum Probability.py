import heapq
from collections import defaultdict


def maxProbability(n: int, edges , succProb, start_node: int, end_node: int) -> float:
    graph = defaultdict(list)
    for i in range(len(edges)):
        a, b = edges[i]
        p = succProb[i]
        graph[a].append([b, -p])
        graph[b].append([a, -p])

    heap = [[-1, start_node]]  # probablity, node
    visit = set()
    max_prob = 0
    while heap:
        prob, node = heapq.heappop(heap)
        prob = -prob
        if node == end_node:
            max_prob = max(max_prob, prob)
        else:
            if node in visit:
                continue
            visit.add(node)
            for a, p in graph[node]:
                new_prob = prob * (-p)
                # if new_prob <= max_prob:
                #     continue
                heapq.heappush(heap, [-new_prob, a])
    return max_prob

print(maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
