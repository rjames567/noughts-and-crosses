# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import os
import time


# ------------------------------------------------------------------------------
# Exceptions
# ------------------------------------------------------------------------------
class CellOccupiedError(Exception):
    def __init__(self):
        super().__init__("The target cell on the board is already occupied")

# ------------------------------------------------------------------------------
# Board Class
# ------------------------------------------------------------------------------
class Board:
    def __init__(self):
        self._grid = [[0 for i in range(3)] for k in range(3)]
        self._piece_lookup = {
            0: " ",
            1: "X",
            -1: "O"
        }

        self._piece_num_lookup = {
            " ": 0,
            "X": 1,
            "O": -1
        }

    def _display_horizontal_line(self):
        print("+---" * 3 + "+")

    def get_empty(self):
        res = []
        for row, i in enumerate(self._grid):
            for col, k in enumerate(i):
                if k == 0:
                    res.append((row, col))

    def display(self):
        for i in self._grid:
            self._display_horizontal_line()
            print("¦ " + " ¦ ".join(self._piece_lookup[k] for k in i) + " ¦")
        self._display_horizontal_line()

    def add_piece(self, row, col, character):
        if self._grid[row][col]:
            raise CellOccupiedError
        self._grid[row][col] = self._piece_num_lookup[character]

    def check_full(self):
        return not sum(i.count(0) for i in self._grid)

    def check_win(self):
        for i in self._grid:
            total = sum(i)
            if total == 3:
                return True, self._piece_lookup[1]
            elif total == -3:
                return True, self._piece_lookup[-1]

        for i in range(3):
            total = sum(k[i] for k in self._grid)
            if total == 3:
                return True, self._piece_lookup[1]
            elif total == -3:
                return True, self._piece_lookup[-1]

        total = sum(self._grid[i][i] for i in range(3))
        if total == 3:
            return True, self._piece_lookup[1]
        elif total == -3:
            return True, self._piece_lookup[-1]

        total = sum(self._grid[i][2 - i] for i in range(3))
        if total == 3:
            return True, self._piece_lookup[1]
        elif total == -3:
            return True, self._piece_lookup[-1]

        return False, None


# ------------------------------------------------------------------------------
# Player Class
# ------------------------------------------------------------------------------
class Player:
    def __init__(self, piece, board, player_num):
        self._piece = piece
        self._board = board
        self._player_num = player_num

    def get_piece(self):
        return self._piece

    def get_move(self):
        valid = False
        print("Player", str(self._player_num) + "'s turn")
        self._board.display()
        while not valid:
            try:
                row = int(input("Enter the row: ")) - 1
                if not 0 <= row <= 2:
                    raise ValueError
                valid = True
            except ValueError:
                print("The row you entered was not valid. Please enter another")
                time.sleep(2)
                clear()
                print("Player", str(self._player_num) + "'s turn")
                self._board.display()

        valid = False
        while not valid:
            try:
                col = int(input("Enter column row: ")) - 1
                if not 0 <= col <= 2:
                    raise ValueError
                valid = True
            except ValueError:
                print("The column you entered was not valid. Please enter another")
                time.sleep(2)
                clear()
                print("Player", str(self._player_num) + "'s turn")
                self._board.display()
                print("Enter the row: " + str(row + 1))

        return row, col


# ------------------------------------------------------------------------------
# Game Class
# ------------------------------------------------------------------------------
class Game:
    def __init__(self):
        self._board = Board()

    def create_players(self, player1_piece, player2_piece):
        self._players = {
            0: Player(player1_piece, self._board, 1),
            1: Player(player2_piece, self._board, 2)
        }

    def play(self):
        player_count = 0
        finished = False

        while not finished:
            valid = False
            while not valid:
                row, col = self._players[player_count].get_move()
                try:
                    self._board.add_piece(row, col, self._players[player_count].get_piece())
                    valid = True
                except CellOccupiedError:
                    print("The chosen cell is occupied. Please chose another.")
                    time.sleep(2)
                    clear()

            player_count = modulo_addition(player_count, 1, 2)

            win, piece = self._board.check_win()
            if win or self._board.check_full():
                finished = True

            clear()

        if win:
            winner = "1"
            if self._players[1].get_piece() == piece:
                winner = "2"
            print("Player", str(winner), "wins.")
        else:
            print("Player 1 and Player 2 drew")


# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------
def modulo_addition(num1, num2, base):
    return (num1 + num2) % base

def clear():
    os.system("clear" if os.name == "posix" else "cls")

# ------------------------------------------------------------------------------
# Play method
# ------------------------------------------------------------------------------
def play():
    clear()
    game = Game()
    game.create_players("X", "O")
    game.play()

if __name__ == "__main__":
    play()