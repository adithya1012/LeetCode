from collections import Counter

def checkInclusion(s1, s2):
    l = 0
    s1_count = Counter(s1)
    s2_count = {}
    for r in range(0, len(s2)):
        if r<len(s1)-1:
            s2_count[s2[r]] = 1+s2_count.get(s2[r], 0)
        else:
            s2_count[s2[r]] = 1+s2_count.get(s2[r], 0)
            if s1_count == s2_count:
                return True
            s2_count[s2[l]] = -1+s2_count.get(s2[l], 0)
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
            l+=1
    return False

print(checkInclusion("ab", "eidbaooo"))