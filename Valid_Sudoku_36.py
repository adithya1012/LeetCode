from collections import defaultdict

def isValidSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)

    for i in range(len(board)):
        for j in range(len(board[0])):
            # rows[i].append(board[i][j]) if board[i][j] != "." else 1
            # cols[j].append(board[i][j]) if board[i][j] != "." else 1
            if board[i][j] == ".":
                continue
            if board[i][j] in rows[i] or board[i][j] in cols[j]:
                print(board[i][j])
                print(rows)
                print(cols)
                return False
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])

    # for row, val in rows.items():
    #     if len(val) != len(set(val)):
    #         # print("returning False 1")
    #         return False

    for col, val in cols.items():
        if len(val) != len(set(val)):
            # print("returning False 2")
            return False
    split = [3, 6, 9]
    for i in split:
        i_first, i_last = i - 3, i
        for j in split:
            j_first, j_last = j - 3, j
            ele = set()
            for inew in range(i_first, i_last):
                for jnew in range(j_first, j_last):
                    if board[inew][jnew] in ele and board[inew][jnew] != ".":
                        # print(ele)
                        # print(i,j)
                        # print(board[inew][jnew])
                        # print(inew, jnew)
                        # print("returning False 3")
                        return False
                    else:
                        ele.add(board[inew][jnew])
    return True
print(isValidSudoku([[".","8","7","6","5","4","3","2","1"],
                     ["2",".",".",".",".",".",".",".","."],
                     ["3",".",".",".",".",".",".",".","."],
                     ["4",".",".",".",".",".",".",".","."],
                     ["5",".",".",".",".",".",".",".","."],
                     ["6",".",".",".",".",".",".",".","."],
                     ["7",".",".",".",".",".",".",".","."],
                     ["8",".",".",".",".",".",".",".","."],
                     ["9",".",".",".",".",".",".",".","."]]))