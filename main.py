from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

# Test against all bots
print("Against Quincy:")
play(player, quincy, 1000, verbose=True)

print("\nAgainst Abbey:")
play(player, abbey, 1000, verbose=True)

print("\nAgainst Kris:")
play(player, kris, 1000, verbose=True)

print("\nAgainst Mrugesh:")
play(player, mrugesh, 1000, verbose=True)