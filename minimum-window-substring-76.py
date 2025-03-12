
def minWindow(s: str, t: str) -> str:
    if not s or not t or len(s)<len(t):
        return ""
    t_count = {}
    t_set = set(t)
    count = len(t_set)
    for i in t:
        t_count[i] = 1+t_count.get(i,0)
        # count += 1

    s_count = {}
    having = 0
    l,r = 0,0
    min_ele = float('inf')
    nl,nr = 0,0
    while r<len(s):
        if s[r] in t_set:
            s_count[s[r]] = 1+s_count.get(s[r],0)
            if s_count[s[r]] == t_count[s[r]]:
                having+=1
        while l<=r and having == count:
            if r-l+1 < min_ele:
                nl,nr = l,r
                min_ele = min(min_ele, r-l+1)
            if s[l] in t_set:
                s_count[s[l]] = -1+s_count.get(s[l],0)
                if s_count[s[l]] < t_count[s[l]]:
                    having -= 1
            l+=1
        r+=1
    return s[nl:nr+1] if min_ele != float('inf') else ""

print(minWindow("a", "a"))