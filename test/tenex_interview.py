# Req:
# - not necery be 3*3, should be n*n
# - all the other constants remaon same
# - 2 players
# - Win, Draw, In_progres
from enum import Enum
from typing import List


# Classes:
# Player, Board, TTT, Simulation(main function)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def change_symbol(self):
        pass

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]

    def place_move(self, i: int,j: int, p: Player):
        if self.board[i][j] is not None:
            self.board[i][j] = p.symbol
            return True
        return False

    def is_winner(self, i: int,j: int, p: Player):

        # row
        negetive = True
        for col in range(self.size):
            if not self.board[i][col] or self.board[i][col] != p.symbol:
                negetive = False
                break
        if negetive == True:
            return True

        negetive = True
        for row in range(self.size):
            if not self.board[row][j] or self.board[row][j] != p.symbol:
                negetive = False
                break
        if negetive == True:
            return True

        negetive = True
        for i in range(self.size):
            if not self.board[i][i] or self.board[i][i] != p.symbol:
                negetive = False
                break
        if negetive == True:
            return True

        

    def is_draw(self):
        pass


class TTT:
    def __init__(self, player: List[Player], size = 3):
        self.board = Board(size)
        self.players = player
        self.player_index = 0
        self.status = "in_progress" # "in_progress" or "won" or "draw"
        self.current_player = self.players[0]

    def switch_player(self):
        pass

    def user_input(self):
        attempt = 0
        while attempt != 5:
            try:
                raw_ip = input("Your Move: ")
                raw_ip = raw_ip.strip()
                row, col = raw_ip.split(",")
                return int(row), int(col)
            except:
                print("invalid input try again")
                attempt += 1
        print("User is not able to give right input")
        return -1, -1


    def play(self):
        print("please enter your move as row, col")
        while self.status != "in_progress":
            row, col = self.user_input()
            # TODO: Validation
            success = self.board.place_move(row, col, self.current_player)
            if not success:
                print("invalid Move")
                continue
            winner = self.board.is_winner(row, col, self.current_player)
            if winner:
                print(f"Player {self.current_player} is the winner !!! ")
                self.status = "Win"
            if self.board.is_draw():
                print(f"!!! Draw match !!! ")
                self.status = "Draw"
            self.switch_player()

        self.status = "in_progress"




if __name__ == "__main__":
    p1 = Player("ABC", "X")
    p2 = Player("XYZ", "Y")

    t = TTT([p1, p2], 3)
    t.play()


