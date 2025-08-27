from board import Board

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

    def solve(self, board):
        self.board = board
        self.load_unsolved()
        print(self.unsolved)