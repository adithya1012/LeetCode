class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []

        def dfs(i):
            if i >= len(nums):
                return False
            if len(stack) == 3:
                return True
            if dfs(i + 1):
                return True
            while stack and stack[-1] >= nums[i]:
                stack.pop()
            stack.append(nums[i])
            state = dfs(i + 1)
            stack.pop()
            return state

        return dfs(0)