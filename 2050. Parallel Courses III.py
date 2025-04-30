
import collections

def minimumTime(n: int, relations, time) -> int:
    graph = collections.defaultdict(list)
    for a,b in relations:
        graph[a].append(b)
    visit = set()
    def dfs(i):
        if i in visit:
            return 0
        if not graph[i]:
            return time[i-1]
        res = 0
        visit.add(i)
        for j in graph[i]:
            res += dfs(j)
        graph[i] = []
        return res+time[i-1]
    res = 0
    for i in range(1, n+1):
        if i not in visit and res < time[i-1]:
            res+=dfs(i)
            # res+=time[i-1]
    return res

# print(minimumTime(5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]))

