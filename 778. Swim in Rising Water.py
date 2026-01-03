import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        heap = [[grid[0][0], 0, 0, -1,-1]]  # waitTime, x, y
        visit = {}
        parent = {}
        while heap:
            wait, x, y, px, py = heapq.heappop(heap)

            if (x, y) in visit:
                continue
            parent[(x, y)] = px, py
            visit[(x, y)] = wait
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                self._print_path(parent, x, y)
                return wait


            for nx, ny in direction:
                nx += x
                ny += y
                if min(nx, ny) < 0 or nx == len(grid) or ny == len(grid[0]) or (nx, ny) in visit:
                    continue
                tmp = max(wait, grid[nx][ny])
                heapq.heappush(heap, [tmp, nx, ny, x, y])
                # parent[(nx,ny)] = (x,y)

    def _print_path(self, parent, x, y):
        path = [(x,y)]
        while (x,y) in parent:
            x,y = parent[(x,y)]
            path.append((x,y))
            if (x,y) == (0,0):
                break

        print(path[::-1])



print(Solution().swimInWater([[0,2],[1,3]]))