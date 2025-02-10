from collections import defaultdict, Counter

# def majorityElement(nums):
#     vals = defaultdict(int)
#     for i in nums:
#         vals[i] += 1
#
#     max_val = 0
#     max_key = 0
#     for i, j in vals.items():
#         if j > max_val:
#             max_val = j
#             max_key = i
#
#     return max_key

'''
O(n) time complexity, but approximately O(n) space complexity
'''

# def majorityElement(nums):
#     key = nums[0]
#     val = 1
#     tmp = 1
#     nums.sort()
#     print(nums)
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             tmp += 1
#         else:
#             if tmp > len(nums)//2:
#                 return nums[i-1]
#             if tmp > val:
#                 val = tmp
#                 key = nums[i-1]
#             tmp = 1
#     if tmp > val:
#         key = nums[-1]
#     return key

'''
This will take a O(nlogn) but takes O(1) space
'''

def majorityElement(nums):
    count = 0
    val = 0
    for i in nums:
        if count == 0:
            val = i
        count += (-1 if val != i else +1)
    return val

'''Boyer-Moore Voting Algorithm
Time complexity: O(n)
Space complexity: O(1)
'''

print(majorityElement([2,2,1,1,1,2,2]))
