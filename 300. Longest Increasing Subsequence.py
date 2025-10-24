class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.res = 0
        stack = []
        def dfs(i):
            if i >= len(nums):
                self.res = max(len(stack), self.res)
                return
            if not stack or stack[-1] > nums[i]:
                stack.append(nums[i])
                dfs(i+1)
                stack.pop()
            dfs(i+1)
        dfs(0)
        return self.res