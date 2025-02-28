
from collections import defaultdict


def fourSum(nums, target):
    res = []
    nums = sorted(nums)
    ele = defaultdict(list)
    pairs = set()
    for i in range(len(nums)):
        # if nums[i] in ele[0]:
        #     continue
        # ele[0].append(nums[i])
        for j in range(i + 1, len(nums)):
            # if nums[j] in ele[1]:
            #     continue
            # ele[1].append(nums[j])
            if (nums[i], nums[j]) in pairs:
                continue
            pairs.add((nums[i], nums[j]))
            l = j + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[j] + nums[l] + nums[r] == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
    return res


print(fourSum([1,0,-1,0,-2,2], 0))