
def lengthOfLongestSubstring(s):
    ele = {s[0]}
    i = 0
    j = 1
    sub_len = 1
    max_len = 1
    while j<len(s):
        if s[j] not in ele:
            # sub_len += 1
            ele.add(s[j])
            max_len = max(max_len, len(ele))
        else:
            sub_len = 0
            while s[i] != s[j]:
                ele.remove(s[i])
                i+=1
            i+=1
        j += 1
    return max_len

# print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))