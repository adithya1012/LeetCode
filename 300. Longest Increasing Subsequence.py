
def lengthOfLIS(nums) -> int:
    res = 0
    stack = []
    def dfs(i):
        if i >= len(nums):
            nonlocal res
            res = max(len(stack), res)
            return
        if not stack or stack[-1] < nums[i]:
            stack.append(nums[i])
            dfs(i+1)
            stack.pop()
        dfs(i+1)
    dfs(0)
    return res

lengthOfLIS([0,1,0,3,2,3])