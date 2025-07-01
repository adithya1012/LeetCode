# https://leetcode.com/discuss/post/6865859/amazon-online-assessment-sde2-jun-2025-b-r3nv/
#
# Q1

def solve(inventory, dispatch1, dispatch2, skip):
    total = dispatch1 + dispatch2
    ans = 0
    skips = []

    for i in inventory:
        i %= total
        if 0 < i <= dispatch1:
            ans += 1
        else:
            i = dispatch2 if i == 0 else i - dispatch1
            skips.append((i + dispatch1 - 1) // dispatch1)

    skips.sort()
    for s in skips:
        if s > skip:
            break
        ans += 1
        skip -= s

    return ans
