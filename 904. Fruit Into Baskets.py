
fruits = [3,3,3,1,2,1,1,2,3,3,4]
tmp = []
visit = set()
def dfs(i, trees, tmp):
    if i >= len(fruits):
        return 0
    res = 0
    if len(trees) < 2 and fruits[i] not in trees:

        trees.add(fruits[i])
        tmp.append((i, fruits[i]))
        res = max(res, 1 + dfs(i + 1, trees, tmp))
        tmp.pop()
        trees.remove(fruits[i])
        res = max(res, dfs(i + 1, trees, tmp))
    elif fruits[i] in trees:
        tmp.append((i, fruits[i]))
        res = max(res, 1 + dfs(i + 1, trees, tmp))
        tmp.pop()
    return res

print(tmp)
print(dfs(0, set(), tmp))