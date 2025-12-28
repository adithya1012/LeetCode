from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges):

        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        q = deque([])
        edge_count = {}
        for i in tree:
            if len(tree[i]) == 1:
                q.append(i)
            else:
                edge_count[i] = len(tree[i])

        while q:
            if n <= 2:
                return list(q)
            for _ in range(len(q)):
                node = q.popleft()
                n-=1
                for i in tree[node]:
                    edge_count[i] -= 1
                    if edge_count[i] == 1:
                        q.append(i)



print(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))    