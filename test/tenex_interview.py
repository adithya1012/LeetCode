# Req:
# - not necery be 3*3, should be n*n
# - all the other constants remaon same
# - 2 players
# - Win, Draw, In_progres
from enum import Enum


# - Board
# - Player
# - game status: Win, Draw, In_progres
# - TicTacto


class Player(Enum):
    PLAYER1="X"
    PLAYER2="Y"

class Board:
    def __init__(self, size=3):
        self.matrix = [[None]*size for i in range(size)]
        self.size = size

    def place_move(self, player: Player, row: int, col:int) -> bool:
        if not self.matrix[row][col]:
            self.matrix[row][col] = player
            return True
        return False

    def is_winner(self) -> bool:
        # row
        for i in range(self.size):
            first = self.matrix[i][0]
            match = True
            for j in range(self.size):
                if first != self.matrix[i][j]:
                    match = False
                    break
            if match:
                return True

        # col
        for j in range(self.size):
            first = self.matrix[j][0]
            match = True
            for i in range(self.size):
                if first != self.matrix[i][j]:
                    match = False
                    break
            if match:
                return True

        # dig
        first = self.matrix[0][0]
        match = True
        for i in range(self.size):
            if first != self.matrix[i][i]:
                match = False
                break
        if match:
            return True

        # opposit-dig
        n = self.size-1
        first = self.matrix[0][n]
        match = True
        for i in range(self.size):
            if first != self.matrix[i][n-i]:
                match = False
                break
        if match:
            return True
        return False

    def is_draw(self) -> bool:



class TTT:
    def __init__(self, size=3):
        self.board = Board(size)
        self.size = size
        self.players = [Player.PLAYER1, Player.PLAYER2]
        self.status = "in_progress" # Win, Draw
        self.player_index = 0

    def switch_player(self):
        self.player_index += 1
        self.player_index = self.player_index % 2

    def play(self):
        print(f"your input should be within {self.size-1}*{self.size-1}")
        while self.status != "in_progress":
            while True:
                raw = input("please enter your Move")
                # TODO: Validation
                row, col = raw.split(",")
                row = int(row)
                col = int(col)
                if self.board.place_move(self.players[self.player_index], row, col):
                    break
                else:
                    print("Invalid Move")

            if self.board.is_winner():
                print(f"Player: {self.players[self.player_index]} is the winner !!!")
                self.status = "Win"

            if self.board.is_draw():
                print(f"Match is Draw")
                self.status = "Draw"

if __name__ == "__main__":
    ttt = TTT(3)
    ttt.play()










