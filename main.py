class Board:
    def __init__(self):
        self._grid = [[0 for i in range(3)] for k in range(3)]
        self._piece_lookup = {
            0: " ",
            1: "X",
            -1: "O"
        }

    def display(self):
        for i in self._grid:
            print("¦ " + " ¦ ".join(self._piece_lookup[k] for k in i) + " ¦")
