# Given two lists of strings, return if list 1 contains anything in list 2.

list1 = [1,2,3,4]
list2 = [3,4, 5,6,7,8]

res = []
list2 = set(list2)
for i in list1:
    if i in list2:
        res.append(i)
print(res)

