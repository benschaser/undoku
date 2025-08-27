from board import Board

def main():
    test_file = "../test/s1.txt"
    board = Board.load_board(test_file)
    board.print_cross_lite(3,5)


if __name__ == "__main__":
    main()