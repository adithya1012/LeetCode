class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque([[]])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q[0].append((i, j))

        visited = set()
        count = 0
        while q:
            print(q)
            vals = q.popleft()
            count += 1
            next_vals = []

            for i, j in vals:
                for ni, nj in direction:
                    ni, nj = ni + i, nj + j
                    if ni == -1 or nj == -1 or ni == row or nj == col or grid[ni][nj] == -1 or grid[ni][nj] == 0 or \
                            grid[ni][nj] < row * col:
                        continue
                    elif grid[ni][nj] == 2147483647:
                        print("HELLOOOO")
                        grid[ni][nj] = count
                        next_vals.append((i, j))
            if next_vals:
                q.append(next_vals)








