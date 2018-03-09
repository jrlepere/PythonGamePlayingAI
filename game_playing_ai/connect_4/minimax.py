import numpy as np
from game_playing_ai.connect_4.utilities import Utilities


class Connect4MiniMax:
    """
    MiniMax implementation to play Connect 4.
    """

    MAX_DEPTH = 6  # Max Depth of the search
    INFINITY = 10000  # Infinity
    NEG_INFINITY = -10000  # Negative Infinity

    @staticmethod
    def get_move(board):
        """
        Gets an optimal move for the passed board configuration.
        :param board: the current board configuration.
                8x8 grid of 1s, 0s, and -1s where
                1  := AI's move
                0  := space
                -1 := opponents move
        :return: a 2 element array representing the [row, col] of the optimal move.
        """

        alpha = Connect4MiniMax.NEG_INFINITY
        beta = Connect4MiniMax.INFINITY
        play = Connect4MiniMax._h_mini_max(board, 0, alpha, beta)
        return np.array([play[1], play[2]])

    @staticmethod
    def _h_mini_max(board, depth, alpha, beta):
        """
        Heuristic MiniMax implementation.
        :param board: the current board configuration.
        :param depth: the current depth of the search.
        :param alpha: alpha component for alpha-beta pruning.
        :param beta: beta component for alpha-beta pruning.
        :return: an optimal move in a 2 element array.
        """

        # Cutoff test
        if (depth == Connect4MiniMax.MAX_DEPTH) or Utilities.terminal_test(board):
            return np.array([Connect4MiniMax._evaluate_board(board)])

        successors = Connect4MiniMax._get_possible_moves(board)
        if depth % 2 == 0:
            # AI's move
            v = np.array([Connect4MiniMax.NEG_INFINITY])
            for successor in successors:
                row = successor[0]
                col = successor[1]
                board[row][col] = Utilities.MAX
                res = Connect4MiniMax._h_mini_max(board, depth + 1, alpha, beta)
                board[row][col] = Utilities.EMPTY
                if res[0] > v[0]:
                    v = np.array([res[0], row, col])
                alpha = max(alpha, v[0])
                if beta <= alpha:
                    return v
            return v
        else:
            # Opponent's move
            v = np.array([Connect4MiniMax.INFINITY])
            for successor in successors:
                row = successor[0]
                col = successor[1]
                board[row][col] = Utilities.MIN
                res = Connect4MiniMax._h_mini_max(board, depth + 1, alpha, beta)
                board[row][col] = Utilities.EMPTY
                if res[0] < v[0]:
                    v = np.array([res[0], row, col])
                beta = min(beta, v[0])
                if beta <= alpha:
                    return v
            return v

    @staticmethod
    def _get_possible_moves(board):
        """
        Gets a list of successors moves for the current board.
        :param board: the current board configuration.
        :return: an array representing the row and column for each possible move.
        """
        moves = []
        for col in range(len(board)):
            for row in range(len(board)-1, -1, -1):
                if board[row][col] == Utilities.EMPTY:
                    moves.append([row, col])
                    break
        return moves

    @staticmethod
    def _evaluate_board(board):
        """
        Gets an evaluation for the board.
        :param board: the current board configuration.
        :return: an evaluation.
        """

        # WINNER TEST - Row Test
        for row in range(len(board)):
            for col in range(len(board) - 3):
                if ((board[row][col] != Utilities.EMPTY) and
                        (board[row][col] == board[row][col + 1]) and
                        (board[row][col + 1] == board[row][col + 2]) and
                        (board[row][col + 2] == board[row][col + 3])):
                    return board[row][col]

        # WINNER TEST - Column Test
        for col in range(len(board)):
            for row in range(len(board) - 3):
                if ((board[row][col] != Utilities.EMPTY) and
                        (board[row][col] == board[row + 1][col]) and
                        (board[row + 1][col] == board[row + 2][col]) and
                        (board[row + 2][col] == board[row + 3][col])):
                    return board[row][col]

        # WINNER TEST - Diagonal Test
        # TODO

        return 0
