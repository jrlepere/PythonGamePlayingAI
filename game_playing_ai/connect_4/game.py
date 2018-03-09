import numpy as np

class Connect4Game:
    """
    Class for playing Connect 4. Main objective is to house the board for the game,
     retrieve moves from the ai/player, and update the board.
    :param board The board will always be represented with respect to the AI.
            That is, 1 will represent a tile for AI and -1 will represent a tile
            for the player. This is to simplify the MiniMax algorithm for AI move
            selection.
    :param human_turn true if it is the humans move, false otherwise.
    """

    def __init__(self, human_first):
        """
        Creates an Connect 4 game instance.
        :param human_first: true if the human (opponent) is going first, false otherwise (ai first). 
        """
        board = np.array([0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0])
        human_turn = human_first

    def play(self):
        """
        Plays a game of Connect 4.
        """
        #TODO
        return 0

