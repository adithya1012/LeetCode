# def removeElement(nums, val):
#     count = 0
#     max_val = max(nums)
#     for i in range(len(nums)):
#         if nums[i] == val:
#             nums[i] += max_val
#             count += 1
#     nums.sort()
#     # print(nums)
#     return len(nums) - count


'''
Time complexity is O(nlogn) because of sorting.
'''
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k



'''
This is O(n) complexity
'''

print(removeElement([0,1,2,2,3,0,4,2], 2))