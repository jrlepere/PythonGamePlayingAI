import numpy as np
from game_playing_ai.connect_4.minimax import Connect4MiniMax
from game_playing_ai.connect_4.utilities import Utilities


class Connect4Game:
    """
    Class for playing Connect 4. Main objective is to house the board for the game,
     retrieve moves from the ai/player, and update the board.
    """

    MAX = 1     # AI's tile value
    MIN = -1    # Opponents tile value
    EMPTY = 0   # Empty tile value

    @staticmethod
    def play(human_turn):
        """
        Plays a game of Connect 4.
        :param human_turn: true if the human (opponent) is going first, false otherwise (ai first).
        """

        board = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0]])

        Utilities.print_board(board)

        while not Utilities.terminal_test(board):
            if human_turn:
                # Human's turn to play

                # Get input
                col = int(input("Col >> "))

                # Test validity
                if not Connect4Game._valid_move(board, col):
                    print("Invalid column: " + str(col))
                    continue

                # Place tile
                for row in range(len(board)-1, -1, -1):
                    if board[row][col] == Connect4Game.EMPTY:
                        board[row][col] = Connect4Game.MIN
                        break

                # Change turn
                human_turn = not human_turn

            else:
                # AI's turn

                # Get and play move
                move = Connect4MiniMax.get_move(board)
                board[move[0]][move[1]] = Connect4Game.MAX

                # Change turn
                human_turn = not human_turn

            Utilities.print_board(board)

    @staticmethod
    def _valid_move(board, col):
        """
        Tests if the move is valid. i.e, tests if the move is on a column with at least one space.
        :param board: the current board configuration.
        :param col: the column to place the tile
        :return: true if the move is valid, false otherwise
        """

        for row in range(len(board)):
            if board[row][col] == Connect4Game.EMPTY:
                return True

        return False
