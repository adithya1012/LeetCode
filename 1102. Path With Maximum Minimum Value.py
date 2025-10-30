
def maximumMinimumPath(grid) -> int:
    # q = deque([0,0, grid[0][0]])
    # visit = set()
    # while q:
    ROW, COL = len(grid), len(grid[0])
    visit = set()
    max_score = 0
    min_val = 0
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def dfs(i, j, val):
        if i == ROW - 1 and j == COL - 1:
            val = min(grid[i][j], val)
            nonlocal min_val
            if min_val < val:
                min_val = val
            return
        if min(i, j) < 0 or i == ROW or j == COL or (i, j) in visit:
            return
        visit.add((i, j))
        for ni, nj in direct:
            ni += i
            nj += j
            dfs(ni, nj, min(grid[i][j], val))
        visit.remove((i, j))

    dfs(0, 0, grid[0][0])
    return min_val

test = False

print(not test)