

def lengthOfLongestSubstring(s):
    max_len = 0
    ele = set()
    i=0
    r=0
    while r<len(s):
        while s[r] in ele:
            ele.remove(s[i])
            i+=1
        ele.add(s[r])
        max_len = max(max_len, len(ele))
        r+=1
    return max_len

print(lengthOfLongestSubstring("abcabcbb"))