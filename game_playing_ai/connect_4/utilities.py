
class Utilities:
    MAX = 1
    MIN = -1
    EMPTY = 0

    @staticmethod
    def terminal_test(board):
        """
        Determines if the board is terminal (win or complete board).
        :param board: the current board configuration.
        :return: true if the board is terminal, false otherwise.
        """

        # Row Test
        for row in range(len(board)):
            for col in range(len(board) - 3):
                if ((board[row][col] != Utilities.EMPTY) and
                        (board[row][col] == board[row][col + 1]) and
                        (board[row][col + 1] == board[row][col + 2]) and
                        (board[row][col + 2] == board[row][col + 3])):
                    return True

        # Column Test
        for col in range(len(board)):
            for row in range(len(board) - 3):
                if ((board[row][col] != Utilities.EMPTY) and
                        (board[row][col] == board[row + 1][col]) and
                        (board[row + 1][col] == board[row + 2][col]) and
                        (board[row + 2][col] == board[row + 3][col])):
                    return True

        # Diagonal Test
        # TODO

        # Full Board Test
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == Utilities.EMPTY:
                    return False

        return True

    @staticmethod
    def print_board(board):
        """
        Prints the board.
        :param board: the board.
        """
        print()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == Utilities.MAX:
                    print('X ', end='')
                elif board[row][col] == Utilities.MIN:
                    print('0 ', end='')
                else:
                    print('_ ', end='')
            print()
