class Board:
    def __init__(self):
        self._grid = [[0 for i in range(3)] for k in range(3)]
        self._piece_lookup = {
            0: " ",
            1: "X",
            -1: "O"
        }

    def _display_horizontal_line(self):
        print("+---" * 3 + "+")

    def _piece_lookup_reverse(self, character):
        return list(self._piece_lookup.keys())[list(self._piece_lookup.values()).index(character)]

    def display(self):
        for i in self._grid:
            self._display_horizontal_line()
            print("¦ " + " ¦ ".join(self._piece_lookup[k] for k in i) + " ¦")
        self._display_horizontal_line()

    def move(self, row, col, character):
        self._grid[row][col] = self._piece_lookup_reverse(character)
