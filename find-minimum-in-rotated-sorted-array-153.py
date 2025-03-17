def findMin(nums) -> int:
    l, r = 0, len(nums)-1
    res = float("inf")
    while l<=r:
        mid = (l+r)//2
        if nums[l] <= nums[r]:
            res = min(nums[l],res)
            # break
        res = min(nums[mid],res)
        if nums[mid] >= nums[l]:
            l = mid+1
        else:
            r = mid-1
    return res



print(findMin([4,5,6,7,0,1,2]))