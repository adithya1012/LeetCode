
def subarraySum(nums, k):
    def dfs(index, sum_val):
        if index == len(nums):
            return 0
        if nums[index]+sum_val == k:
            print(index)
            return 1
        return dfs(index+1, nums[index]+sum_val)
    res = 0
    for i in range(len(nums)):
        # print(i)
        res += dfs(i, 0)
    if k == 0:
        return res+1
    else:
        return res

print(subarraySum([1,-1,0], 0))