
def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (r + l) // 2
        if nums[m] == target:
            return True
        if nums[l] < nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        elif nums[m] < nums[r]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            l = l + 1
    return False

print(search([1,1,1,1,1,1,1,1,1,13,14,15,1,1,1,1,1,1,1,1,1,1], 13))