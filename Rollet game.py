import random


def roll_dice():
    min_val = 1
    max_val = 6
    return random.randint(min_val, max_val)


while True:  # number of players
    players = input("Enter number of players (2-6): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 6:
            break
        else:
            print("Number of players must be between 2 and 6.")
    else:
        print("Invalid input. Please enter a number between 2 and 6.")

max_score = 100
players_score = [0] * players

while max(players_score) < max_score:  # game
    for player_id in range(players):  # initialization
        print("\nPlayer number", player_id + 1, "turn has just started!")
        print("Your total score is:", players_score[player_id], "\n")
        current_score = 0

        while True:  # scoring
            should_roll = input("Would you like to roll? (y/n) ")
            if should_roll != 'y':
                break
            score = roll_dice()
            if score == 1:
                current_score = 0
                print("Oops! You rolled a 1. You lose all your points for this turn.")
                break
            else:
                current_score += score
                print("You rolled:", score)
                print("Your score for this turn is:", current_score)

        players_score[player_id] += current_score
        print("Your total score is:", players_score[player_id])

    max_score = max(players_score)
    if max_score >= 100:
        winner_id = players_score.index(max_score)
        print("\nPlayer number", winner_id + 1,
              "is the winner with a score of:", max_score)
        break
