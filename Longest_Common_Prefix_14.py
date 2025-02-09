def longestCommonPrefix(strs):

    ''' This will not work for al the test cases'''
    # common = ""
    # for i in range(len(strs) - 1):
    #     for j in range(min(len(strs[i]), len(strs[i + 1]))):
    #         if i == 0:
    #             if strs[i][j] == strs[i + 1][j]:
    #                 common += strs[i][j]
    #             else:
    #                 break
    #         else:
    #             if not (len(common) < j and strs[i][j] == strs[i + 1][j] == common[j]):
    #                 common = common[:j + 2]
    #                 break
    # return common

    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if s[i] != strs[0][i]:
                return res
        res += strs[0][i]

print(longestCommonPrefix(["flower","flow","flight"]))

"""
Time complexity is O(n*m)
n: length of strs
m: length of max string inside the strs
"""