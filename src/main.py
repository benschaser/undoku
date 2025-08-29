from board import Board
from solver import Solver
from solver import clear_terminal

def main():
    test_file = "../test/s1.txt"
    board = Board.load_board(test_file)
    # board.print_cross_lite(3,5)

    solver = Solver()
    solver.solve(board)
    clear_terminal()
    board.print()



if __name__ == "__main__":
    main()