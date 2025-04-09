
def numDecodings(s):
    def dfs(i):
        if i == len(s):
            return 1
        if i > len(s)-1 or s[i] == "0":
            return 0


        res = dfs(i + 1)
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
            res += dfs(i + 2)
        return res

    return dfs(0)

print(numDecodings("226"))