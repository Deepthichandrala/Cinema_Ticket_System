import random
snakes = {16: 6, 47: 26, 49: 11, 61: 8, 64: 7, 67: 45, 87: 24, 93: 73, 95: 65, 98: 79}
ladders = {1: 38, 4: 14, 9: 31, 17: 34, 28: 84, 36: 44, 50: 77, 71: 91,75:97, 80: 100}
def roll_dice():
    return random.randint(1, 6)
def move_player(player, steps):
    player += steps
    if player in snakes:
        print("Oops! You got swallowed by a snake!")
        player = snakes[player]
    elif player in ladders:
        print("Congratulations! You climbed a ladder!")
        player = ladders[player]
    return player
def won(player):
    return player == 100
def start_game():
    player1_position = 0
    player2_position = 0
    current_player = 1

    while True:
        input("Player {}, press Enter to roll the dice...".format(current_player))
        steps = roll_dice()
        print("You rolled:", steps)

        if current_player == 1:
            player1_position = move_player(player1_position, steps)
            print("Player 1 is at position", player1_position)
            if won(player1_position):
                print("Player 1 has won!")
                break
            current_player = 2
        else:
            player2_position = move_player(player2_position, steps)
            print("Player 2 is at position", player2_position)
            if won(player2_position):
                print("Player 2 has won!")
                break
            current_player = 1

start_game()