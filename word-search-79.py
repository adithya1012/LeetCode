
def exist(board, word):
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    row = len(board)
    col = len(board[0])
    visited = set()
    def dfs(word_i, i, j):
        if word_i == len(word):
            return True

        if i == -1 or j == -1 or i == row or j == col or word[word_i] != board[i][j] or (i, j) in visited:
            return False
        visited.add((i,j))
        for ni, nj in direction:
            ni, nj = ni + i, nj + j
            if dfs(word_i + 1, ni, nj):
                print(ni, nj, board[ni][nj])
                return True
        visited.remove((i, j))
        return False

    for i in range(row):
        for j in range(col):
            if dfs(0, i, j):
                return True
    return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
