from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_triangle = [triangle[0]]
        for bottom in range(1, len(triangle)):
            top = min_triangle[bottom-1]
            res = []
            for i in range(len(top)):
               res.append(min(triangle[bottom][i]+top[i], triangle[bottom][i+1]+top[i]))
            min_triangle.append(res)
        print(min_triangle)
        return min(min_triangle[-1])


Solution().minimumTotal([[-1],[2,3],[1,-1,-3]])