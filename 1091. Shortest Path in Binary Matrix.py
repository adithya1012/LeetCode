
def shortestPathBinaryMatrix(grid) -> int:
    dummy = [[0] * len(grid[0]) for _ in range(len(grid))]
    row, col = len(grid), len(grid[0])
    if grid[0][0] != 0 or grid[row - 1][col - 1] != 0:
        return -1

    def dfs(i, j):
        if i == len(grid) or j == len(grid[0]):
            return float("inf")
        if grid[i][j] == 1:
            return float("inf")
        if i == row - 1 and j == col - 1:
            return 1
        dummy[i][j] = 1 + min(dfs(i + 1, j), dfs(i + 1, j + 1), dfs(i, j + 1))
        return dummy[i][j]

    dfs(0, 0)
    if dummy[0][0] == float("inf"):
        return -1
    else:
        return dummy[0][0]

print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))