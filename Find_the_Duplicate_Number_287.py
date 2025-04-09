def findDuplicate(nums):
    i = 0

    while True:
        if not nums[nums[i] - 1]:
            return nums[i]
        if i + 1 == nums[i]:
            nums[i] = None
            i = i + 1
        else:
            nums[i] = nums[nums[i] - 1]
            nums[nums[i] - 1] = None


print(findDuplicate([1,3,4,2,2]))