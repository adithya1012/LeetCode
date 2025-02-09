# def groupAnagrams(strs):
#     values = {}
#
#     for i in range(len(strs)):
#         i_sort = "".join(sorted(strs[i]))
#         if i_sort in values:
#             values[i_sort].append(strs[i])
#         else:
#             values[i_sort] = [strs[i]]
#     res = []
#     for i, j in values.items():
#         res.append(j)
'''
Above solution works but having O(m*nlogn) time complexity. nlogn is because of the sorting each string
m = length of strs
n = max length of any string
'''

from collections import defaultdict, Counter
def groupAnagrams(strs):
    values = defaultdict(list)

    for i in strs:
        # i_sort = "".join(sorted(strs[i]))
        count = [0]*26
        for s in i:
            count[ord(s)-ord("a")+1] += 1
        values[tuple(count)].append(i)
    return list(values.values())

'''
time complexity is O(m*n)

m = length of strs
n = max length of any string

there no sorting in this code. 

I tried using Counter but it is not working because dist is not hashable (also set and list is not hashable).

'''


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
