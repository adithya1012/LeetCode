
def threeSum(nums):
    nums.sort()
    res = []
    for i,first in enumerate(nums):
        if i>0 and first == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l<r:
            total = first+nums[l]+nums[r]
            if total == 0:
                res.append([first, nums[l], nums[r]])
                l+=1
                # r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
            elif total > 0:
                r-=1
            else:
                l+=1
    return res

threeSum([-1,0,1,2,-1,-4])

