
def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def dfs(i, total, val):
        if total == target:
            res.append(val.copy())
            return
        if total > target or i >= len(candidates):
            return

        val.append(candidates[i])
        dfs(i + 1, total + candidates[i], val)
        val.pop()
        # i += 1
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        # if i < len(candidates):
        # val.append(candidates[i])
        dfs(i + 1, total, val)
        # val.pop()

    dfs(0, 0, [])
    return res

print(combinationSum2([10,1,2,7,6,1,5], 8))