import heapq
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # graph_dict = defaultdict(list)
        # for i in range(len(graph)):

        heap = [[0, i, [(-1,i)], str(i)] for i in range(len(graph))]  # path_count, node, visit_node
        while heap:
            path_count, node, path, visit_node = heapq.heappop(heap)
            if len(visit_node) == len(graph):
                print(path)
                return path_count
            else:
                # path_count += 1
                path.append((path_count, node))
                visit_node.add(node)
                for i in graph[node]:
                    heapq.heappush(heap, [path_count+1, i, path, visit_node])



# print(Solution().shortestPathLength([[1,2,3],[0],[0],[0]]))

graph = [1,2,3]
heap = []

for i in range(len(graph)):
    if graph[i]:
        heap.append([0, i, {i}])

print(heap)
heap[0][2].add(3)
print(heap)
