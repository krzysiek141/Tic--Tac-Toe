import numpy as np


class Player:

    winner = None

    def __init__(self):
        self.symbol = ""

    def check_for_victory(self, board):
        # turn into boolean matrix
        bool_board = (board == self.symbol)
        # check rows
        for row in bool_board:
            vict = np.all(row)
            if vict:
                self.__class__.winner = self
                break
        # check columns
        for i in range(bool_board.shape[1]):
            vict = np.all(bool_board[:, i])
            if vict:
                self.__class__.winner = self
                break
        #check diagonals
        diagonal_1 = np.diagonal(bool_board)
        diagonal_2 = np.diagonal(np.fliplr(bool_board))
        if np.all(diagonal_1) or np.all(diagonal_2) == True:
            self.__class__.winner = self 

    def give_coordinates(self):
        incorrect_nums = True
        while incorrect_nums:
            coor_row = int(input(f"Player '{self.symbol}' choose the row number\n>>> "))
            coor_column = int(input(f"Player '{self.symbol}' choose the column number\n>>> "))
            if (coor_row >= 1) and (coor_row <= 3) and (coor_column >= 1) and (coor_column <= 3):
                incorrect_nums = False
            else:
                print("Row and column numbers must be in the range of <1, 3>. Choose again.")
        return (coor_row, coor_column)