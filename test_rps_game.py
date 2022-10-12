'''Unittest for rps_game.py'''
# Student name: Sinmei Li (Kabi)
# Student ID: S360233
import unittest
from rps_game import RPSGame


class RPSGameTestCase(unittest.TestCase):
    '''test case for ROCK PAPER SCISSOR game'''
    rps_game = RPSGame()

    def test_player_input(self):
        '''Check the player's input is from 1 to 3'''
        # Valid input test from number 1 to 3#
        self.assertTrue(self.rps_game.is_input_valid(1))
        self.assertTrue(self.rps_game.is_input_valid(2))
        self.assertTrue(self.rps_game.is_input_valid(3))
        # Invalid input test for out of range numbers and strings
        self.assertFalse(self.rps_game.is_input_valid(5))
        self.assertFalse(self.rps_game.is_input_valid(-1))
        self.assertFalse(self.rps_game.is_input_valid("ROCK"))

    def test_player_choice(self):
        '''Check if the player's input matches the actions'''
        # Valid input test from number 1 to 3#
        self.assertEqual(self.rps_game.player_choice(1), "ROCK")
        self.assertEqual(self.rps_game.player_choice(2), "PAPER")
        self.assertEqual(self.rps_game.player_choice(3), "SCISSOR")

        # Invalid input test for out of range numbers and strings
        self.assertFalse(self.rps_game.player_choice(0))
        self.assertFalse(self.rps_game.player_choice("ROCK"))

    def test_game_rule(self):
        '''Check the result of winner'''
        # Test when player and computer play the same action
        self.assertIsNone(self.rps_game.round_win("PAPER", "PAPER"))
        self.assertIsNone(self.rps_game.round_win("ROCK", "ROCK"))
        self.assertIsNone(self.rps_game.round_win("SCISSOR", "SCISSOR"))

        # Test when player and computer play the different action
        # (SCISSOR wins PAPER, ROCK wins SCISSOR, PAPER wins ROCK)
        self.assertEqual(self.rps_game.round_win("SCISSOR", "PAPER"), "Player")
        self.assertEqual(self.rps_game.round_win("SCISSOR", "ROCK"), "Computer")
        self.assertEqual(self.rps_game.round_win("PAPER", "SCISSOR"), "Computer")
        self.assertEqual(self.rps_game.round_win("PAPER", "ROCK"), "Player")
        self.assertEqual(self.rps_game.round_win("ROCK", "PAPER"), "Computer")
        self.assertEqual(self.rps_game.round_win("ROCK", "SCISSOR"), "Player")


if __name__ == '__main__':
    unittest.main()
