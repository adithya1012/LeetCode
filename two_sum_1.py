def twoSum(nums, target):
    diff = {}
    for i in range(len(nums)):
        if target-nums[i] in diff:
            return [diff[target-nums[i]], i]
        diff[nums[i]] = i

print(twoSum([2, 7, 11, 15], 9))