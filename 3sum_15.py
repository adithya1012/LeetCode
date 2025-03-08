
# def threeSum(nums):
#     res = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i],nums[j],nums[k]]) not in res:
#                     res.append(sorted([nums[i],nums[j],nums[k]]))
#     return res


'''
Above solution is time limit exceeding. O(n cube)
'''

# def threeSum(nums):

