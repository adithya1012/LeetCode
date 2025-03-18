
def search(nums, target):
    l = 0
    r = len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[l]:
            if target < nums[l]:
                l = mid+1
            else:
                r = mid -1
        else:
            if target < nums[r]:
                l = mid-1
            else:
                l = mid+1
    return -1

print(search([1], 0))