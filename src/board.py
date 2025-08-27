RESET = "\033[0m"
LITE = "\033[7m"
HL = "---------+-----------+---------"

class Board:
    def __init__(self, grid):
        self.grid = grid
    
    @classmethod
    def load_board(cls, filepath):
        with open(filepath) as f:
            rows = [
                [int(ch) if ch.isdigit() else 0 for ch in line.strip()] 
                for line in f if line.strip()
            ]
        
        return cls(rows)

    def get_cell(self, x, y):
        return self.grid[y][x]
    
    def get_row(self, y):
        return self.grid[y]
    
    def get_col(self, x):
        col = []
        for row in self.grid:
            col.append(row[x])
        return col

    def set_cell(self, x, y, val):
        self.grid[y][x] = val

    def print_row(self, row_index, full_lite, col_lite):
        r = self.grid[row_index]
        if (full_lite):
            print(LITE + "{}  {}  {}  |  {}  {}  {}  |  {}  {}  {}".format(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]) + RESET)
        elif (col_lite != -1):
            formatted_row = "{}  {}  {}  |  {}  {}  {}  |  {}  {}  {}".format(
                r[0] if col_lite != 0 else LITE + str(r[0]) + RESET,
                r[1] if col_lite != 1 else LITE + str(r[1]) + RESET,
                r[2] if col_lite != 2 else LITE + str(r[2]) + RESET,
                r[3] if col_lite != 3 else LITE + str(r[3]) + RESET,
                r[4] if col_lite != 4 else LITE + str(r[4]) + RESET,
                r[5] if col_lite != 5 else LITE + str(r[5]) + RESET,
                r[6] if col_lite != 6 else LITE + str(r[6]) + RESET,
                r[7] if col_lite != 7 else LITE + str(r[7]) + RESET,
                r[8] if col_lite != 8 else LITE + str(r[8]) + RESET,
            )
            print(formatted_row)
        else:
            print("{}  {}  {}  |  {}  {}  {}  |  {}  {}  {}".format(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))

    def print(self):
        self.print_row(0, False, 2)
        self.print_row(1, True, 2)
        self.print_row(2, False, 2)
        print(HL)
        self.print_row(3, False, 2)
        self.print_row(4, False, 2)
        self.print_row(5, False, 2)
        print(HL)
        self.print_row(6, False, 2)
        self.print_row(7, False, 2)
        self.print_row(8, False, 2)
    