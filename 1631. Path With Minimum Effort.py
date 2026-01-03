import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]):
        direction = [[0,1], [1,0], [-1,0], [0,-1]]
        heap = [[0,0,0]] # max_effort_in_path , x, y
        # visit = set()
        dist = [[float("inf")] * len(heights[0]) for _ in range(len(heights))]
        dist[0][0] = 0
        parent = {}
        while heap:
            effort, x, y = heapq.heappop(heap)
            print(effort, x, y)
            if x == len(heights)-1 and y == len(heights[0])-1:
                return effort, self._build_path(x,y, parent)
            if dist[x][y] < effort:
                continue
            dist[x][y] = effort
            for nx, ny in direction:
                nx+=x
                ny+=y
                if min(nx,ny) < 0 or nx == len(heights) or ny == len(heights[0]):
                    continue
                max_effort = max(effort, abs(heights[x][y]-heights[nx][ny]))
                if max_effort < dist[nx][ny]:
                    dist[nx][ny] = max_effort
                    parent[(nx,ny)] = (x,y)
                    heapq.heappush(heap, [max_effort, nx, ny])
        return -1, []

    def _build_path(self, x,y, parent):
        path = [(x,y)]
        while (x,y) in parent:
            px, py = parent[(x,y)]
            path.append((px,py))
            x,y = px, py

        return path

print(Solution().minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))
