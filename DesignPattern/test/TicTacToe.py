
class Player:
    def __init__(self, id):
        self.id = id

    def player_id(self):
        return self.id


class Board:
    def __int__(self, row, col):
        self.row = row
        self.col = col
        self.board = [[0 for _ in range(col)] for _ range(row)]

    def insert(self, p, r, c):
        pid = p.id
        if self.board[r][c] != 0:
            return "Invalid Move"
        self.board[r][c] = pid
        if self.check_winner():
            # TODO: print the board and reset it to all zeros
            return f"{pid} is the winner"
        return "Inserted Next Move ! "
