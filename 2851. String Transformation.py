
def numberOfWays(s, t, k):
    count = 0

    def arrange(s, i):
        return s[i:] + s[:i]

    def rearrange(s, kt):
        if s == t and kt == k:
            nonlocal count
            count += 1
            return
        if kt >= k:
            return

        for i in range(1, len(s)):
            stmp = arrange(s, i)
            rearrange(stmp, kt + 1)
        return

    rearrange(s, 0)
    return count

print(numberOfWays("goxoq", "dfqgl", 244))

# 326024901249