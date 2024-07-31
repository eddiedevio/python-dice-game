import random


def roll_die():
    return random.randint(1, 6)  # returns random number between 1-6


player_turn = random.randint(1, 2)
player_1_score = []  # player 1 score stored in a list
player_2_score = []  # player 2 score stored in a list
target_score = 100 # target score determines the winner
consecutive_rolls = 0  # tracks consecutive times player rolls

while True:
    if player_turn == 1:
        player_1_roll = roll_die()
        print(f'Player 1, you rolled a: {player_1_roll}')
        if player_1_roll > 1:
            consecutive_rolls += 1
            player_1_score.append(player_1_roll)
            total_score = sum(player_1_score)
            print(f'Player 1, you have a score of: {total_score}')

            if total_score >= target_score:
                print(f'Congratulations, Player 1. You have won the game with a score of {total_score}!')
                break

            if consecutive_rolls >= 3:
                decision = input('You are on a streak. Do you want to continue? (yes/no): ')
                if decision.lower() == 'no':
                    consecutive_rolls = 0
                    player_turn = 2
                    print(f'Player 2, it is your turn.')
                continue  # Go to the next iteration to handle Player 2's turn
        else:
            player_1_score = []
            print('Oops, you rolled a 1. You have lost all points.')
            consecutive_rolls = 0
            player_turn = 2
            print(f'Player 2, it is your turn.')
            continue  # Go to the next iteration to handle Player 2's turn

    if player_turn == 2:
        player_2_roll = roll_die()
        print(f'Player 2, you rolled a: {player_2_roll}')
        if player_2_roll > 1:
            consecutive_rolls += 1
            player_2_score.append(player_2_roll)
            total_score = sum(player_2_score)
            print(f'Player 2, you have a score of: {total_score}')

            if total_score >= target_score:
                print(f'Congratulations, Player 2. You have won the game with a score of {total_score}!')
                break

            if consecutive_rolls >= 3:
                decision = input('You are on a streak. Do you want to continue? (yes/no): ')
                if decision.lower() == 'no':
                    consecutive_rolls = 0
                    player_turn = 1
                    print(f'Player 1, it is your turn.')
                continue  # Go to the next iteration to handle Player 1's turn
        else:
            player_2_score = []
            print('Oops, you rolled a 1. You have lost all points.')
            consecutive_rolls = 0
            player_turn = 1
            print(f'Player 1, it is your turn.')
            continue  # Go to the next iteration to handle Player 1's turn
