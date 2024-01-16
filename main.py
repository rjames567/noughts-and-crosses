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

    def display(self):
        for i in self._grid:
            self._display_horizontal_line()
            print("¦ " + " ¦ ".join(self._piece_lookup[k] for k in i) + " ¦")
        self._display_horizontal_line()

    def move(self, row, col, character):
        if self._grid[row][col]:
            raise CellOccupiedError
        self._grid[row][col] = self._piece_num_lookup[character]

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
    def __init__(self, piece):
        self._piece = piece

    def get_piece(self):
        return self._piece

    def get_move(self):
        valid = False
        while not valid:
            try:
                row = int(input("Enter the row: ")) - 1
                if not 0 <= row <= 2:
                    raise ValueError
                valid = True
            except ValueError:
                print("The row you entered was not valid. Please enter another")

        valid = False
        while not valid:
            try:
                col = int(input("Enter column row: ")) - 1
                if not 0 <= col <= 2:
                    raise ValueError
                valid = True
            except ValueError:
                print("The column you entered was not valid. Please enter another")

        return row, col
