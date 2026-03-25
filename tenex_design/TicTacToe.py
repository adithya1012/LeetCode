from enum import Enum


# ─────────────────────────────────────────
# 1. ENUMS
# ─────────────────────────────────────────
class Player(Enum):
    X = "X"
    O = "O"


class GameState(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    WIN         = "WIN"
    DRAW        = "DRAW"


# ─────────────────────────────────────────
# 2. BOARD
# ─────────────────────────────────────────
class Board:
    def __init__(self, size: int = 3):
        self.size  = size
        self.grid  = [[None] * size for _ in range(size)]  # None = empty

    def display(self):
        print()
        for r, row in enumerate(self.grid):
            cells = []
            for cell in row:
                cells.append(cell.value if cell else ".")
            print("  " + " | ".join(cells))
            if r < self.size - 1:
                print("  " + "-" * (self.size * 4 - 3))
        print()

    def place(self, row: int, col: int, player: Player) -> bool:
        if not self._in_bounds(row, col):
            print("  Invalid position — out of bounds.")
            return False
        if self.grid[row][col] is not None:
            print("  Cell already occupied — try again.")
            return False
        self.grid[row][col] = player
        return True

    def is_full(self) -> bool:
        return all(self.grid[r][c] is not None
                   for r in range(self.size)
                   for c in range(self.size))

    def check_winner(self, player: Player) -> bool:
        g, n = self.grid, self.size

        # Check all rows
        for r in range(n):
            if all(g[r][c] == player for c in range(n)):
                return True

        # Check all columns
        for c in range(n):
            if all(g[r][c] == player for r in range(n)):
                return True

        # Check main diagonal (top-left → bottom-right)
        if all(g[i][i] == player for i in range(n)):
            return True

        # Check anti-diagonal (top-right → bottom-left)
        if all(g[i][n - 1 - i] == player for i in range(n)):
            return True

        return False

    def _in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.size and 0 <= col < self.size


# ─────────────────────────────────────────
# 3. PLAYER
# ─────────────────────────────────────────
class HumanPlayer:
    def __init__(self, player: Player):
        self.player = player

    def get_move(self, board: Board) -> tuple[int, int]:
        while True:
            try:
                raw = input(f"  Player {self.player.value} → enter row,col (0-indexed): ")
                r, c = map(int, raw.strip().split(","))
                return r, c
            except ValueError:
                print("  Invalid input — enter as row,col e.g. 1,2")


# ─────────────────────────────────────────
# 4. GAME
# ─────────────────────────────────────────
class TicTacToe:
    def __init__(self, size: int = 3):
        self.board       = Board(size)
        self.players     = [
            HumanPlayer(Player.X),
            HumanPlayer(Player.O),
        ]
        self.current_idx = 0           # index into self.players
        self.state       = GameState.IN_PROGRESS

    @property
    def current_player(self) -> HumanPlayer:
        return self.players[self.current_idx]

    def switch_turn(self):
        self.current_idx = 1 - self.current_idx   # toggles 0 ↔ 1

    def play(self):
        print("\n=== TicTacToe ===")
        print("  Enter moves as  row,col  (both 0-indexed)")
        self.board.display()

        while self.state == GameState.IN_PROGRESS:
            p = self.current_player

            # Get a valid move
            while True:
                row, col = p.get_move(self.board)
                if self.board.place(row, col, p.player):
                    break                          # valid move placed

            self.board.display()

            # Check win
            if self.board.check_winner(p.player):
                self.state = GameState.WIN
                print(f"  Player {p.player.value} wins!")
                return

            # Check draw
            if self.board.is_full():
                self.state = GameState.DRAW
                print("  It's a draw!")
                return

            self.switch_turn()


# ─────────────────────────────────────────
# 5. ENTRY POINT
# ─────────────────────────────────────────
if __name__ == "__main__":
    game = TicTacToe(size=3)   # change size=4 or 5 for bigger board
    game.play()
