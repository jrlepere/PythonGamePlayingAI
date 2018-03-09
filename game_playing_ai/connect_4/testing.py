import numpy as np
from game_playing_ai.connect_4.game import Connect4Game
from game_playing_ai.connect_4.utilities import Utilities

board = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0],
                  [0, 1, 0, 0, 0, 0, 1, 0],
                  [1, 0, 0, 0, 0, 0, 0, 1]])

if __name__ == "__main__":
    human_first = True
    Connect4Game.play(human_first)
    #print(Utilities.terminal_test(board))
