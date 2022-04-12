import unittest
import tictactoe_reinforcement
import numpy as np
import pandas as pd

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


if __name__ == "__main__":
    unittest.main()




