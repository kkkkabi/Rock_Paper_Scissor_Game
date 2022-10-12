Rock_Paper_Scissor_Game
====

This is a rock-aper-scissor game project written in Python. Player will compete with computer, and the first to get 5 points wins the game. In this project I use TDD method to develop and test this program.

Objective: 
----
This game allows a single player to play with a computer without time limitation. The game is easy to learn and is for all aged people. This is also my first Python project that implements TDD method.

Requirement of this game:
----
1.	The computer randomly picks one of the options of scissor, paper, and rock.
2.	Player is given the option to pick one of the options of scissor, paper, and rock.
3.	One point is given to the winner.
4.	The first to get 5 points wins the game. 
5.	At the end of the game, the total number of rounds played will also be displayed.
6.	Once the winner is determined, the player is asked to quit or restart the game.
7.	Player can also quit the game at any time.


Tools used in this project:
----
•	Linting tools: Flake8 and Pylint<br>
•	TDD automated test tool: PyUnit<br>

How to play the game:
----
run call_rps_game.py<br>
The player chooses of the options between scissor, paper, and rock. Then this compared against computer’s selection and determine who the winner is. 
Game rules are as below:<br>
•	rock vs paper -> paper wins<br>
•	rock vs scissor -> rock wins<br>
•	paper vs scissor -> scissor wins<br>


Game procedure are as follows:
----
1.	Computer randomly picks one of the options of scissor, paper, and rock.
2.	Player types a number to pick one of the options of scissor, paper, and rock.
3.	Compare player’s selection against computer’s selection.
4.	Determine the winner of this round, and 1 point is given to the winner.
5.	The first to get 5 points is the winner of this game.
6.	At the end, player can choose to continue playing the game or quit the game.
