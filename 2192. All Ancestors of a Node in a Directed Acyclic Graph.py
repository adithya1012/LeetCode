import collections


def getAncestors(n: int, edges):
    graph = collections.defaultdict(list)
    edges.sort()
    for frm, to in edges:
        graph[frm].append(to)

    res = [[] for _ in range(10)]

    visit = set()

    def dfs(node, prev):
        # if node in visit:
        #     return
        for i in prev:
            res[node].append(i)
        if node not in graph:
            return
        prev.append(node)
        for i in graph[node]:
            dfs(i, prev)
        prev.pop()
        visit.add(node)

    for i in range(n):
        dfs(i, [])
    return res

print(getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))