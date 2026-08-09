# Given two arrays A and B, remove the duplicates from A which are present in B. (can be duplicates too)
# Follow up 1 : How do you maintain the order of the elements that are returned (their actual order in A)
# Follow up 2: Maintain the reverse order.
from collections import Counter


def calculate(A, B):
    b_count = Counter(B)
    res = []
    for a in A:
        if a in b_count:
            b_count[a]-=1
            if not b_count[a]:
                del b_count[a]
        else:
            res.append(a)
    return res


a = [1,2,3,3,4]
b = [1,2,2,2,3]
print(calculate(a, b))
