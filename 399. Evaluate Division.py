from collections import defaultdict
from typing import List


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = defaultdict(list)
    i = 0
    for a, b in equations:
        graph[a].append([b, values[i]])
        graph[b].append([a, 1 / values[i]])
        i += 1
    print(graph)
    visit = set()

    def dfs(a, b, val):
        visit.add(a)
        for i, v in graph[a]:
            if i not in visit:
                tmp = val * v
                if i == b:

                    return tmp
                else:
                    ans = dfs(i, b, tmp)
                    if ans:
                        return ans
        visit.remove(a)
        return False

    res = []
    for a, b in queries:
        if a not in graph or b not in graph:
            res.append(-1)
        
        else:
            ans = dfs(a, b, 1)
            if ans:
                res.append(ans)
            else:
                res.append(-1)
    return res


print(calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))