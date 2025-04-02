def getSubstringCount(s: str) -> int:
    # count = 0
    # prev_group = 0
    # curr_group = 1
    #
    # for i in range(1, len(s)):
    #     if s[i] == s[i - 1]:
    #         curr_group += 1
    #     else:
    #         count += min(prev_group, curr_group)
    #         prev_group = curr_group
    #         curr_group = 1
    #
    # count += min(prev_group, curr_group)
    # return count

    j = 1
    count = [0] * 2
    count[int(s[0])] += 1
    res = {}
    while j<len(s):
        if s[j] == s[j-1]:
            count[int(s[j])] += 1
            j+=1
        else:
            if count[0] == count[1] and count[0] != 0:
                res
                count = [0] * 2
            if min(count) != 0:
                j=j+1
                count = [0]*2




# Example usage:
s = "011001"
print(getSubstringCount(s))  # Output: 4