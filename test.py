# import unittest
#
#
# def add2No(a, b):
#     return a + b
#
#
# class TestCaseExecution(unittest.TestCase):
#     def test_add2Normal(self):
#         self.assertEqual(add2No(10, 20), 30)
#
#     def test_add2Zero(self):
#         self.assertEqual(add2No(0, 0), 0)
#
#     def test_add2Negetive(self):
#         self.assertEqual(add2No(-10, -20), -30)
#
#
#
# if "__mani__" == __name__:
#     unittest.main()
# #
# # def trap(heights):
# #     left = [0] * len(heights)
# #     right = [0] * len(heights)
# #     left[0] = heights[0]
# #     right[-1] = heights[-1]
# #
# #     for i in range(1, len(heights)):
# #         left[i] = max(left[i-1], heights[i])
# #
# #     for i in range(len(heights)-2, -1, -1):
# #         right[i] = max(right[i+1], heights[i])
# #
# #     res = []
# #     for i in range(len(heights)):
# #         res.append(min(left[i], right[i]))
# #     print("heights:",heights)
# #     print("left:   ",left)
# #     print("right:  ",right)
# #     print("res:    ",res)
# # trap([0,1,0,2,1,0,1,3,2,1,2,1])


def test(nums):
    zero = -1
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero] = nums[i]
            zero += 1
    for i in range(zero, len(nums)):
        nums[i] = 0
    retr

