# Amazon recently launched a new game, Fruit Crush! In this game, you are allowed to choose two dissimilar fruits and crush them. Each type of fruit is represented as an integer in an array. Formally you can choose any two unequal integers in the array and delete them.

# Given an array fruits of size n, return the minimum possible number of fruits left after the given operation is performed any number of times.
# Example
# n = 5
# fruits = [3, 3, 1, 1, 2]

# Fruits 1 (banana) and 2 (pineapple) can be crushed first, followed by numbers 1 (banana) and 3 (orange). Only 3 (orange) remains in the array, hence the answer is 1.

def min_fruits(fruits):
    stack = []
    for i in fruits:
        if stack and stack[-1] != i:
            stack.pop()
        else:
            stack.append(i)
    return len(stack)

print(min_fruits([3, 3, 1, 1, 2]))
print(min_fruits([]))
print(min_fruits([1,1,1,1]))
