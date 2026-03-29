import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) == 0:
        return "R"

    # Detect random opponent (Abbey)
    if len(opponent_history) > 60:
        r = opponent_history.count("R")
        p = opponent_history.count("P")
        s = opponent_history.count("S")

        total = len(opponent_history)

        # If distribution is nearly equal → random player
        if abs(r - total/3) < total*0.15 and abs(p - total/3) < total*0.15:
            return random.choice(["R", "P", "S"])

    # Pattern-based prediction (length 3)
    n = 3
    if len(opponent_history) >= n:
        pattern = "".join(opponent_history[-n:])
        counts = {"R": 0, "P": 0, "S": 0}

        for i in range(len(opponent_history) - n):
            seq = "".join(opponent_history[i:i+n])
            if seq == pattern:
                next_move = opponent_history[i+n]
                counts[next_move] += 1

        if sum(counts.values()) > 0:
            predicted = max(counts, key=counts.get)
        else:
            predicted = random.choice(["R", "P", "S"])
    else:
        predicted = random.choice(["R", "P", "S"])

    # Counter move
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[predicted]