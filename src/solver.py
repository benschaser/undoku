from board import Board
import time

def clear_terminal():
    print("\033[2J\033[H", end="")


class Solver:
    def __init__(self):
        self.unsolved = {}

    def load_unsolved(self): 
        for r in range(0, 9, 1):
            for c in range(0, 9, 1):
                if (self.board.get_cell(c, r) == 0):
                    self.unsolved[(c, r)] = []
    
    def get_possible(self, x, y):
        row = self.board.get_row(y)
        col = self.board.get_col(x)
        box = self.board.get_box(x, y)
        self.unsolved[(x, y)] = []
        for i in range(1, 10, 1):
            if (i not in row) and (i not in col) and (i not in box):
                self.unsolved[(x, y)].append(i)
    
    def solve_cell(self, x, y):
        if (len(self.unsolved[(x, y)]) == 1):
            self.board.set_cell(x, y, self.unsolved[(x, y)][0])
            return True
        return False
    
    def remove_solved(self):
        to_remove = []
        for (x, y) in self.unsolved.keys():
            if (len(self.unsolved[(x, y)]) == 1):
                to_remove.append((x, y))
        for coord in to_remove:
            del self.unsolved[coord]
            
    def solve(self, board):
        self.board = board
        self.load_unsolved()
        solves_made = False

        # first round, try to solve all cells with only one possibility
        for (x, y) in self.unsolved.keys():
            clear_terminal()
            self.board.print_cross_lite(x, y)
            self.get_possible(x, y)
            solves_made = self.solve_cell(x, y) or solves_made
            time.sleep(0.2)
        self.remove_solved()
        while (len(self.unsolved) > 0):
            if not solves_made:
                # insert temp values
                print("No more direct solves possible, need to implement guessing")
                break
                
            else:
                solves_made = False
                for (x, y) in list(self.unsolved.keys()):
                    clear_terminal()
                    self.board.print_cross_lite(x, y)
                    self.get_possible(x, y)
                    solves_made = self.solve_cell(x, y) or solves_made
                    time.sleep(0.2)

            self.remove_solved()




            
        
