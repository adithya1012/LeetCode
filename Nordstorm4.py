# You are given:
#
# 👉 A string of digits only
#
# s = "25525511135"
# Length: typically between 1 and 12
# Only contains characters '0'–'9'
# Return:
#
# 👉 All possible valid IP addresses that can be formed from the string.
#
# Each IP address:
#
# Has 4 parts
# Each part is separated by "."
# Each part must be a valid number


res = []
s = "25525511135"
def dfs(i, cur, rem):
    if rem == 0 and i == len(s):
        res.append(cur[1:])
        return

    if i >= len(s) or rem*3 < len(s[i:]) or rem == 0:
        return

    for j in range(3):
        if i+j < len(s) and int(s[i:i+j+1]) <= 255:
            dfs(i+j+1, cur+"-"+s[i:i+j+1], rem-1)
print(dfs(0, "", 4))
print(res)
