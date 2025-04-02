from collections import deque

def openLock(deadends, target) -> int:
    if "0000" in deadends:
        return -1

    def children(lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
            digit = str((int(lock[i]) - 1 + 10) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
        print(res)
        return res

    q = deque([("0000", 0)])
    visit = set(deadends)

    while q:
        lock, turns = q.popleft()
        if lock == target:
            return turns
        for child in children(lock):
            if child not in visit:
                visit.add(child)
                q.append((child, turns + 1))
    return -1

print(openLock(["0201","0101","0102","1212","2002"], "0202"))