import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        direction = [[0,1], [1,0], [-1,0], [0,-1]]
        heap = [[0,0,0]] # max_effort_in_path , x, y
        visit = set()
        while heap:
            effort, x, y = heapq.heappop(heap)
            if x == len(heights)-1 and y == len(heights[0])-1:
                return effort
            if (x,y) in visit:
                continue
            visit.add((x,y))
            for nx, ny in direction:
                nx+=x
                ny+=y
                if min(nx,ny) < 0 or nx == len(heights) or ny == len(heights[0]) or (nx,ny) in visit:
                    continue
                max_effort = max(effort, abs(heights[x][y]-heights[nx][ny]))
                heapq.heappush(heap, [max_effort, nx, ny])
        return -1, []

