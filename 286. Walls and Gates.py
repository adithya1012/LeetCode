from collections import deque

class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        ROW, COL = len(rooms), len(rooms[0])

        q = deque([])

        for i in range(ROW):
            for j in range(COL):
                if rooms[i][j] == 0:
                    q.append([i, j])

        distance = -1
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visit = set()
        while q:
            distance += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                rooms[i][j] = distance
                visit.add((i, j))
                for ni, nj in direction:
                    ni += i
                    nj += j
                    if min(ni, nj) < 0 or ni == ROW or nj == COL or rooms[ni][nj] != INF or (ni, nj) in visit:
                        continue
                    q.append([ni, nj])
            for i in rooms:
                print(i)
            print()
        # for i in rooms:
        #     print(i)


Solution().wallsAndGates(rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])