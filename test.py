
import collections


def canFinish(numCourses: int, prerequisites) -> bool:
    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    visit = set()

    def dfs(i):
        if i in visit:
            return False

        for j in graph[i]:
            if not dfs(j):
                return False

        return True

    for i in range(numCourses):
        if i not in visit:
            if not dfs(i):
                return False
    return True

print(canFinish(2, [[1,0]]))
