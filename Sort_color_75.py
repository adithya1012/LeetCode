def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    i = 0
    r = len(nums) - 1

    def swap(i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    while i < r:
        if nums[i] == 0:
            swap(i, l)
            l += 1
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
        i += 1
    print(nums)

sortColors([2,0,2,1,1,0])