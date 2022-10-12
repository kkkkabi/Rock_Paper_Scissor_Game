'''This is ROCK PAPER SCISSOR game.
If you want to play the game, please run Call_RPSGame.py'''
import random
import sys


class RPSGame():
    '''Where player and computer pick up actions from'''
    Action_list = {1: "ROCK", 2: "PAPER", 3: "SCISSOR"}

    def is_input_valid(self, player_choice):
        '''Check if player has valid input from 1 to 3.'''
        try:
            player_choice = int(player_choice)
        except ValueError:
            return False
        if player_choice in RPSGame.Action_list:
            return True
        return False

    def player_choice(self, player_choice):
        '''Return the action that player choose'''
        if RPSGame.is_input_valid(RPSGame, player_choice):
            player_choice = int(player_choice)
            player_act = RPSGame.Action_list[player_choice]
            return player_act
        return False

    def computer_choice(self):
        '''Return the action that computer randomly pick'''
        computer_no = random.randint(1, 3)
        computer_choice = RPSGame.Action_list[computer_no]
        return computer_choice

    def round_win(self, player_act, com_act):
        '''Compare actions played by player and computer,
           and then return who is the winner'''
        if player_act == com_act:   # No winner, if it's a tie.
            return None
        if player_act == "ROCK" and com_act == "SCISSOR":
            return "Player"
        if player_act == "PAPER" and com_act == "ROCK":
            return "Player"
        if player_act == "SCISSOR" and com_act == "PAPER":
            return "Player"
        return "Computer"

    def game_start(self):
        '''Set the rules to end the competition and determine who winner is.
           the first to get 5 scores wins the competition
           Reveal the winner and display the number of rounds played.'''
        player_score = 0
        com_score = 0
        round_number = 0

        while player_score < 5 and com_score < 5:
            prompt = "Choose [1]ROCK, [2]PAPER, [3]SCISSOR, [4]End the game :"
            player_input = input(prompt)
            if player_input == "4":     # To end the game, input 4
                print('''
===== Game End =====
You choose to end the game. See you next time!\n''')
                sys.exit()

            # If wrong input, ask the player to choose again
            elif not RPSGame.is_input_valid(RPSGame, player_input):
                print("Please choose your action again.\n")

            elif RPSGame.is_input_valid(RPSGame, player_input):
                round_number += 1
                com_act = RPSGame.computer_choice(RPSGame)
                player_act = RPSGame.player_choice(RPSGame, player_input)
                winner = RPSGame.round_win(RPSGame, player_act, com_act)

                # Give 1 point to winner in each round.
                if winner is None:    # If it's a tie, no one gets a point.
                    winner = "No one"
                elif winner == "Player":
                    player_score += 1
                elif winner == "Computer":
                    com_score += 1

                # Output results of the round
                print(f"------ Round {round_number} -----")
                print(f"{winner} wins this round!")
                print(f"You play [{player_act}]")
                print(f"Computer plays [{com_act}]")
                print(f"Your score is {player_score}.")
                print(f"Computer's score is {com_score}.\n")

        # Show the result of the comptition
        game_winner = str()
        if player_score > com_score:
            game_winner = "You"
        else:
            game_winner = "Computer"
        print("====== Game ends ======")
        print(f"The winner is {game_winner}!")
        print(f"The total rounds are {round_number}.\n")
