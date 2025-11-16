from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = set()
        unsafe = set()

        def dfs(node):
            if node in visit:
                return False  # cycle detected
            visit.add(node)
            if node in safe:
                return True  # the node will leads to the terminal node hence Safe
            if node in unsafe:
                return False  # the node will leads to a cycle so unsafe
            for i in graph[node]:
                if not dfs(i):
                    return False
            visit.remove(node)
            return True  # No node leads to cycle hence safe node

        for i in range(len(graph)):
            visit = set()
            if i not in safe and i not in unsafe:
                if dfs(i):
                    safe = safe | visit
                else:
                    unsafe = unsafe | visit
        return list(safe)


print(Solution().eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]) )
