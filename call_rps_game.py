''' Run to start RPSgame'''
# Student name: Sinmei Li (Kabi)
# Student ID: S360233

# Game ruels:
# 1. There are 3 actions ([1]ROCK, [2]PAPER, and [3]SCISSOR),and
#    both player and computer select one action of the list
# 2. Compare the actions to get the winner of the round
#    If player and computer play the same actions, it's a tie.
#    -ROCK wins SCISSOR
#    -PAPER wins ROCK
#    -SCISSOR wins PAPER
# 3.One point is given to the winner in each round.
# 4.The first to get 5 points wins the game.
# 5.Player can quit the game at anytime by input number 4.
import sys
from rps_game import RPSGame

while True:  # If player wants to continue, restart the game.
    print('''
=====Welcome to play ROCK PAPER SCISSOR game=====
Rules: The first one to get 5 points in winner.
Let's start!''')
    RPSGame.game_start(RPSGame)  # Start the game
    restart = input("Restart the game? (Y/N) ")
    if restart.upper() == "Y":
        continue
    sys.exit()
