RESET = "\033[0m"
LITE = "\033[7m"
HL = "├──────────┼───────────┼──────────┤"
TL = "┌──────────┬───────────┬──────────┐"
BL = "└──────────┴───────────┴──────────┘"
def cell_f(num):
        return num if num != 0 else "□"

class Board:
    def __init__(self, grid):
        self.grid = grid
    
    @classmethod
    def load_board(cls, filepath):
        with open(filepath) as f:
            rows = [
                [int(ch) if ch.isdigit() else 0 for ch in line.strip() if ch != " "] 
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
    
    def get_box(self, x, y):
        box = []
        box_start_x = (x // 3) * 3
        box_start_y = (y // 3) * 3
        for r in range(box_start_y, box_start_y + 3, 1):
            for c in range(box_start_x, box_start_x + 3, 1):
                box.append(self.grid[r][c])
        return box

    def set_cell(self, x, y, val):
        self.grid[y][x] = val

    
    
    def print_row(self, row_index, full_lite, col_lite):
        r = self.grid[row_index]
        if (full_lite):
            print("│" + LITE + " {}  {}  {}  │  {}  {}  {}  │  {}  {}  {} ".format(
                cell_f(r[0]), 
                cell_f(r[1]), 
                cell_f(r[2]), 
                cell_f(r[3]), 
                cell_f(r[4]), 
                cell_f(r[5]), 
                cell_f(r[6]), 
                cell_f(r[7]), 
                cell_f(r[8])
            ) + RESET + "│")
        elif (col_lite != -1):
            formatted_row = "│ {}  {}  {}  │  {}  {}  {}  │  {}  {}  {} │".format(
                cell_f(r[0]) if col_lite != 0 else LITE + str(cell_f(r[0])) + RESET,
                cell_f(r[1]) if col_lite != 1 else LITE + str(cell_f(r[1])) + RESET,
                cell_f(r[2]) if col_lite != 2 else LITE + str(cell_f(r[2])) + RESET,
                cell_f(r[3]) if col_lite != 3 else LITE + str(cell_f(r[3])) + RESET,
                cell_f(r[4]) if col_lite != 4 else LITE + str(cell_f(r[4])) + RESET,
                cell_f(r[5]) if col_lite != 5 else LITE + str(cell_f(r[5])) + RESET,
                cell_f(r[6]) if col_lite != 6 else LITE + str(cell_f(r[6])) + RESET,
                cell_f(r[7]) if col_lite != 7 else LITE + str(cell_f(r[7])) + RESET,
                cell_f(r[8]) if col_lite != 8 else LITE + str(cell_f(r[8])) + RESET,
            )
            print(formatted_row)
        else:
            print("│ {}  {}  {}  │  {}  {}  {}  │  {}  {}  {} │".format(
                cell_f(r[0]), 
                cell_f(r[1]), 
                cell_f(r[2]), 
                cell_f(r[3]), 
                cell_f(r[4]), 
                cell_f(r[5]), 
                cell_f(r[6]), 
                cell_f(r[7]), 
                cell_f(r[8])
            ))

    def print(self):
        print(TL)
        self.print_row(0, False, -1)
        self.print_row(1, False, -1)
        self.print_row(2, False, -1)
        print(HL)
        self.print_row(3, False, -1)
        self.print_row(4, False, -1)
        self.print_row(5, False, -1)
        print(HL)
        self.print_row(6, False, -1)
        self.print_row(7, False, -1)
        self.print_row(8, False, -1)
        print(BL)
    
    def print_cross_lite(self, x, y):
        print(TL)
        self.print_row(0, y == 0, x)
        self.print_row(1, y == 1, x)
        self.print_row(2, y == 2, x)
        print(HL)
        self.print_row(3, y == 3, x)
        self.print_row(4, y == 4, x)
        self.print_row(5, y == 5, x)
        print(HL)
        self.print_row(6, y == 6, x)
        self.print_row(7, y == 7, x)
        self.print_row(8, y == 8, x)
        print(BL)
    