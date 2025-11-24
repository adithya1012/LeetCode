from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()

        def dfs(i, total):
            max_sum = 0

            if i == len(nums):
                return max_sum

            if total + nums[i] % 3 == 0:
                max_sum = total + nums[i]

            consider = dfs(i + 1, total + nums[i])
            skip = dfs(i + 1, total)

            max_sum = max(consider, skip, max_sum)

            return max_sum

        return dfs(0, 0)

Solution().maxSumDivThree(nums = [1,2,3,4,4])


