from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        def dfs(i):
            # if i == len(nums)-1:
            #     return 0
            if i >= len(nums) - 1:
                return 0
            res = float("inf")
            if nums[i] == 0:
                return res
            for j in range(i, i + nums[i] + 1):
                res = min(res, 1 + dfs(j))
            return res

        return dfs(0)

print(Solution().jump([2,3,1,1,4]))