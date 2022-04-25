import unittest
import tictactoe_reinforcement
import numpy as np
import pandas as pd
from unittest.mock import Mock
from unittest.mock import patch
import unittest

# Only one test case possible in tictactoe_reinforcement.py
class TestTicTacToe(unittest.TestCase):

    # Test case for the get_latest_board_value
    def test_get_latest_board_values(self):
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])), str(np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])), str(np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]])), str(np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]])), str(np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]])), str(np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])), str(np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]])), str(np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]])), str(np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 0, 0], [0, 0, 0], [0, 1, 0]])), str(np.array([[0, 0, 0], [0, 0, 0], [0, 1, 0]]).reshape(3*3)))
        self.assertEqual(tictactoe_reinforcement.PlayerTraining.get_latest_board_values(self, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]])), str(np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]]).reshape(3*3)))

    # Check for the available
    # Based on the board value the available positions must be calculated
    def test_available_positions(self):
        board_one =  tictactoe_reinforcement.TicTacToe("playerone", "player_two")
        board_one.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        assert board_one.available_position() == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2,2)]
        board_one.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
        assert board_one.available_position() == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
        board_one.board = np.array([[0, 0, 0], [0, 0, 0], [0, -1, 1]])
        assert board_one.available_position() == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]
        board_one.board = np.array([[1, 0, 0], [0, 0, 0], [0, -1, 1]])
        assert board_one.available_position() == [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)]
        board_one.board = np.array([[1, -1, 1], [0, -1, 0], [0, -1, 1]])
        assert board_one.available_position() == [(1, 0),(1, 2), (2, 0)]

    # Unit testing for checking the winners, loosers and draws
    def test_check_win(self):
        the_board = tictactoe_reinforcement.TicTacToe("playerone", "player_two")
        the_board.board = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
        assert the_board.check_win() == 1
        the_board.board = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
        assert the_board.check_win() == 1
        the_board.board = np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]])
        assert the_board.check_win() == 1
        the_board.board = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        assert the_board.check_win() == 1
        the_board.board = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        assert the_board.check_win() == 1
        the_board.board = np.array([[-1, -1, -1], [0, 0, 0], [0, 0, 0]])
        assert the_board.check_win() == -1
        the_board.board = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
        assert the_board.check_win() == -1
        the_board.board = np.array([[-1, 0, 0], [-1, 0, 0], [-1, 0, 0]])
        assert the_board.check_win() == -1
        the_board.board = np.array([[1, -1, 1], [-1, 1, -1], [-1,1, -1]])
        assert the_board.check_win() == 0

    # Unit testing using python mock functions
    


if __name__ == "__main__":
    unittest.main()







