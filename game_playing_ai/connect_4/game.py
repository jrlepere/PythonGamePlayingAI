from game_playing_ai.connect_4.minimax import Connect4MiniMax
from game_playing_ai.connect_4.utilities import Utilities


class Connect4Game:
    """
    Class for playing Connect 4.
    """

    @staticmethod
    def get_ai_move(board):
        """
        Gets the AI's move from the current configuration.
        :param board: the current board configuration
        """
        return Connect4MiniMax.get_move(board)

    @staticmethod
    def is_valid_move(board, col):
        """
        Tests if the move is valid. i.e, tests if the move is on a column with at least one space.
        :param board: the current board configuration.
        :param col: the column to place the tile
        :return: the row where the tile will land location, -1 if invalid
        """

        for row in range(len(board)-1, -1, -1):
            if board[row][col] == Utilities.EMPTY:
                return row

        return -1

    @staticmethod
    def convert_board_string(s_board):
        board = [[], [], [], [], [], [], [], []]
        row = 0
        col = 0
        for line in s_board.split(" "):
            line = line.replace("[","").replace("]","").strip()
            if (line == "0") or (line == "1") or (line == "-1"):
                board[row].append(int(line))
                col += 1
                if col == 8:
                    col = 0
                    row += 1
        return board
