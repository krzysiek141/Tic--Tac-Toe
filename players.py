import numpy as np


class Player:
    def __init__(self):
        self.symbol = ""

    def check_for_victory(self, board):
        # check rows
        for row in (board == self.symbol):
            vict = np.all(row)
            return True if vict == True
        # check columns
        for i in range(board.shape[1]):
            vict = np.all(board[:, i])
            return True if vict == True 
        #check diagonals   
        return False
    
    @staticmethod
    def give_coordinates():
        cor_row = input("Choose the row number\n>>>")
        cor_column = input("Choose the column number\n>>>")
        return [cor_row, cor_column]