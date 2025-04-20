
def subarraySum(nums, k) -> int:
    count = 0
    visit = set()
    def dfs(i, val):
        if val == k:
            nonlocal count
            count += 1
            # return
        # if val > k or i >= len(nums) or (i,val) in visit:
        #     return
        visit.add((i,val))
        if i + 1 < len(nums):
            dfs(i + 1, val + nums[i + 1])
            dfs(i + 1, nums[i + 1])

    dfs(0, nums[0])
    return count

print(subarraySum([1,-1,0], 0))