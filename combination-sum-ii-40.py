
def combinationSum2(candidates, target):
    res = set()
    def backtrack(i, ele, total):
        if total == target:
            res.add(tuple(sorted(ele[:])))
            return
        if total > target or i >= len(candidates):
            return
        ele.append(candidates[i])
        backtrack(i+1, ele, total+candidates[i])
        ele.pop()
        backtrack(i+1, ele, total)
    backtrack(0, [], 0)
    res = [list(i) for i in res]
    return res

print(combinationSum2([1,2,3,4,5], 9))

