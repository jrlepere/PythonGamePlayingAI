import numpy as np


class Connect4MiniMax:
    """
    MiniMax implementation to play Connect 4.
    """

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
        row = 0
        col = 0
        return np.array([row, col])

    @staticmethod
    def _h_mini_max(board):
        """
        Heuristic MiniMax implementation.
        :param board: the current board configuration.
        :return: an optimal move in a 2 element array.
        """

        return np.array([0, 0])

    @staticmethod
    def _get_possible_moves(board):
        """
        Gets a list of successors moves for the current board.
        :param board: the current board configuration.
        :return: an array representing the row and column for each possible move.
        """
        return np.array([0, 0])

    @staticmethod
    def _evaluate_board(board):
        """
        Gets an evaluation for the board.
        :param board: the current board configuration.
        :return: an evaluation.
        """
        return 0

    @staticmethod
    def _terminal_test(board, depth):
        """
        Determines if the board is terminal (win or complete board).
        :param board: the current board configuration.
        :param depth: the current depth of the search.
        :return: true if the board is terminal, false otherwise.
        """
        return False
