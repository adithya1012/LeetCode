import collections


def validTree(n, edges):
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(i, parent):
        if i in visit:
            return False
        visit.add(i)
        for j in graph[i]:
            if j != parent and not dfs(j, i):
                return False
        return True

    for i in range(n):
        visit = set()
        if not dfs(i, -1):
            return False
    return True


