def maxDistinctElements(nums, k: int) -> int:
    nums.sort()
    start = nums[0] - k
    res = 0

    for i in range(len(nums)):
        if start in range(nums[i] - k, nums[i] - k + 1):
            start += 1
            res += 1
        elif start < nums[i] - k:
            start = nums[i] - k + 1
            res += 1
        # elif start > nums[i]+k:
        #     pass
    print(res)
    return res

maxDistinctElements([1,2,2,3,3,4], 2)

