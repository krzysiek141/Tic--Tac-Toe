from players import Player

import numpy as np

player_1 = Player()
player_1.symbol = input("Choose the symbol for the first player\n>>> ")
player_2 = Player()
player_2.symbol = input("Choose the symbol for the second player\n>>> ")

board = np.array([["", "", ""],
                 ["", "", ""],
                 ["", "", ""]])

victory = False
while not victory:
    print(board)

    player_1.give_coordinates()
    victory = player_1.check_for_victory(board)

    player_2.give_coordinates()

    print("check for victory 2")