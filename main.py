from players import Player
from board import Board


def take_a_turn(player: Player):
    board.show()
    while True:
        coordinates = player.give_coordinates()
        if board.is_occupied(coordinates[0], coordinates[1]) == False:
            break
        else:
            print("This square is already occupied. Choose another one.")
    board.update(coordinates[0], coordinates[1], player.symbol)
    player.check_for_victory(board.core)


player_1 = Player()
player_1.symbol = input("Choose the symbol for the first player\n>>> ")
player_2 = Player()
player_2.symbol = input("Choose the symbol for the second player\n>>> ")

board = Board()

run_the_game = True
while run_the_game:
    take_a_turn(player_1)
    if not player_1.victory:
        take_a_turn(player_2)
        if player_2.victory:
            winner = player_2
            run_the_game = False
    else:
        winner = player_1
        run_the_game = False
board.show()
print("Bye bye")