import random

def play(player1, player2, num_games, verbose=False):
    p1_score = 0
    p2_score = 0
    prev_play1 = ""
    prev_play2 = ""

    for _ in range(num_games):
        move1 = player1(prev_play2)
        move2 = player2(prev_play1)

        prev_play1 = move1
        prev_play2 = move2

        if move1 == move2:
            continue

        if (
            (move1 == "R" and move2 == "S") or
            (move1 == "S" and move2 == "P") or
            (move1 == "P" and move2 == "R")
        ):
            p1_score += 1
        else:
            p2_score += 1

    win_rate = p1_score / num_games * 100

    print(f"Player1 win rate: {win_rate:.2f}%")
    return win_rate


# Bots
def quincy(prev_play):
    return "R"


def abbey(prev_play):
    return random.choice(["R", "P", "S"])


def kris(prev_play):
    return "P"


def mrugesh(prev_play):
    return "S"