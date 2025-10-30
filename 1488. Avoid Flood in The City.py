import collections

def avoidFlood(rains):
    lakes = set()
    candry = set()
    empty = collections.deque([])
    res = [-1] * len(rains)
    for j in range(len(rains)):
        i = rains[j]
        if i > 0:
            if i in lakes:
                return []
            if i in candry and not empty:
                return []
            if i in candry:
                index = empty.popleft()
                res[index] = i
                candry.remove(i)
            lakes.add(i)
        else:
            candry = candry.union(lakes)
            lakes = set()
            empty.append(j)
            res[j] = 1
    return res


avoidFlood()