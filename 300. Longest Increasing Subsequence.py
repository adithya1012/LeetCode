from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            consider = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    consider = max(consider, 1 + dfs(j))
            memo[i] = consider
            return consider

        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i))
        print(memo)
        return res


# print(Solution().lengthOfLIS([4,10,4,3,8,9]))

a = [3,4,2,5,1]
print(a)
print(sorted(a))