import collections



def minWindow(s, t):
    tcount = collections.defaultdict(int)
    for i in t:
        tcount[i] += 1
    have, need = len(tcount), 0
    resi, resj = -1, -1
    minWindowLen = float("inf")
    l, r = 0, 0
    scount = collections.defaultdict(int)
    while r < len(s):
        if s[r] in tcount:
            scount[s[r]] += 1

            if scount[s[r]] == tcount[s[r]]:
                need += 1

            while need == have and l <= r:
                if (r - l + 1) < minWindowLen:
                    minWindowLen = r - l + 1
                    resi, resj = l, r
                if s[l] in scount:
                    scount[s[l]] -= 1
                    if scount[s[l]] < tcount[s[l]]:
                        need -= 1
                l += 1
        r += 1
    return s[resi:resj + 1]


print(minWindow("ADOBECODEBANC", "ABC"))

