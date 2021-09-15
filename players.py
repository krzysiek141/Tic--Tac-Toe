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
    
    @staticmethod
    def give_coordinates():
        cor_row = int(input("Choose the row number\n>>> "))
        cor_column = int(input("Choose the column number\n>>> "))
        return (cor_row, cor_column)