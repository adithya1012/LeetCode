# The team at an Amazon warehouse is given a task to optimize the packing of a set of boxes with different IDs. Each box is labeled with an ID, and these boxes are currently arranged in a single row from left to right, where the id of the ith box is represented by the string s_id consisting of digits from 0 to 9 inclusive. To make the packing more efficient, the team can perform the following operation any (possibly zero) number of times:
#
# • Choose an index i and remove the digit s_id[i]. Then insert the box with ID min(s_id[i] + 1, 9) on any position (at the beginning, at the end, or in between any two adjacent boxes) in the row.
# Given a string s_id, find the lexicographically minimal string of boxes using these operations.
# Note: A string X is lexicographically smaller than a string Y of the same length if and only if in the first position where X and Y differ, the string X has a smaller digit than the corresponding digit in Y.
# Example
# Given, s_id = "26547".
#
# Delete 5 and insert 6 in the 4th position of the string
# Delete 6 from the 2nd position and insert 7 in the 4th position of the string
# Hence, the string returned is "24677". It can be proved that this is the lexicographically minimal string possible.
#
# Function Description
# Complete the function getMinimumString in the editor below. getMinimumString has the following parameter:
# string s_id: the ID of the boxes
#
#
# Explanation
#
# Here, s_id = "34892".
#
# The series of operations that shall be performed are:
#
# Delete 3 and insert 4 at the end of the string. So the resulting string
# is 48924",
#
# Delete 4 and insert 5 at the end of the string. So the resulting string
# is 89245"
#
# Delete 8 and insert 9 at the end of the string. So the resulting string
# is "92459"
#
# Delete 9 and insert 9 at the end of the string. So the resulting string
# is "24599".
#
# Hence, the string returned is "24599". It can be proved that this is the lexicographically minimal string possible.
#
# Answer the above in python code

