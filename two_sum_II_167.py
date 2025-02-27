
# def twoSum(numbers, target):
#     numbers_set = set(numbers)
#
#     for i in range(len(numbers)):
#         if target - numbers[i] in numbers_set:
#             for j in range(i + 1, len(numbers)):
#                 if numbers[j] == target - numbers[i]:
#                     return [i + 1, j + 1]


'''
Solving using 2 pointers
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j = j - 1
            else:
                i += 1


