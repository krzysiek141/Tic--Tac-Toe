import numpy as np
import ascii_art 

class Board:

    def __init__(self):
        self.core = np.array([[" ", " ", " "],
                              [" ", " ", " "],
                              [" ", " ", " "]]) 

    def update(self, row_num: int, col_num: int, symbol):
        self.core[row_num - 1, col_num - 1] = symbol

    def show(self):
        matrix_elements = [element for list in self.core for element in list]
        board = ascii_art.board.format(*matrix_elements)
        print(board)

    def is_occupied(self, row_num, col_num):
        if self.core[row_num - 1, col_num - 1] != " ":
            return True
        else:
            return False
