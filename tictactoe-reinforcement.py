"""
Author: Shrikrishna Joisa
Creted on: 2022-06-04
Last Updated on: 2022-06-04

"""


from tokenize import String
from turtle import position
import pandas as pd
import numpy as np
import logging
import pickle5 as pickle

# Tic toe using reinforcement learning (Q-learning)
# We will use feed forward network to approximate the Q-function and use the epsilon-greedy policy to select the next action.

# Episilion-greedy policy uses the prior knowledge and the current state to select the next action.

"""
Logging:
    All the logging data is stored under a file name called "tictactoe-reinforcement.log"
    Message saving format : [date and time] [level] [message]
    Time format : %H:%M:%S
    With minimum message level set to Debug INFO
"""

logging.basicConfig(filename='tictactoe-reinforcement.log', level=logging.INFO, filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S')

# Initialize board values for the game
TOTAL_NUMBER_OF_ROWS = 3
TOTAL_NUMBER_OF_COLUMNS = 3
THE_BOARD = TOTAL_NUMBER_OF_COLUMNS * TOTAL_NUMBER_OF_ROWS


class TicTacToe:


    """
        Initialize the board, player, winner, ended, latest board state, has the game ended state
        and initial board valeu is zero, player one move value is 1 and player two move value is 2
    """

    def __init__(self, player_one, player_two):
        self.board = np.zeros((TOTAL_NUMBER_OF_ROWS, TOTAL_NUMBER_OF_COLUMNS))
        self.player_one = player_one
        self.player_two = player_two
        self.game_has_ended = False
        self.winner = None
        self.latest_board_state = None
        self.player_one_symbol = 1   # when the player takes the first move, the symbol is 1
        self.player_two_symbol = 2       # when the player takes the second move, the symbol is 2


    def play_game(self, number_of_rounds):
        for i in range(number_of_rounds):
            while (self.game_has_ended == False) :
                # Player one moves
                position = self.available_position()
                logging.info("The available positions are" + str(position))
                player_one_choose_move = self.player_one.choose_move(position, self.board, self.player_one_symbol)
                self.game_has_ended = True


    def available_position(self):
        # we need to store the availanle positon in the form of matrix
        # append the only position having the value 0 to the matrix, rest else is filled
        position = []
        for i in range(TOTAL_NUMBER_OF_ROWS):
            for k in range(TOTAL_NUMBER_OF_COLUMNS):
                if self.board[i, k] == 0:
                    position.append([i, k])
        return position



"""
This class includes the trainng and testing methods for the Q-learning algorithm

"""
class PlayerTraining:

    """
    This method is used to train the Q-learning algorithm for the players
    Add the intial state and the all the Q-learning parameters like learning rate, discount factor, epsilon
    """
    def __init__(self, player_identifier):
        self.player_name = player_identifier
        self.position_taken = []
        self.learning_rate = 0.3
        self.discount_rate = 0.9
        self.exploratory_move = 0.3  # make a random move to experience all the states present in the game
        self.greedy_move = 0.7 # To maximize the rewards
        self.position_value = {} # state position value dictionary

    """
        Uniformly choose a random move, an exploratory move where the player takes the move randomly to go through all the possiblile state
        The data is uniformly distributed with the help of uniform method & compared with the expolatory move
    """
    def choose_move(self, position, current_board_state, symbol):
        # make a random move
        # get the random index from the position
        # get the the particular index from the availabel positon using position[index]
        if np.random.uniform(0,1) <= self.exploratory_move:
            id = np.random.choice(len(position))
            choosen_move = position[id]
        else:
            # make a greedy move to maximize the rewards
            max_value = -999
            for p in position:
                next_board = current_board_state.copy()
                next_board[p] = symbol
                next_board_state = self.get_latest_board_values(next_board)
                value = 0 if self.position_value.get(next_board_state) is None else self.position_value.get(next_board_state)
                # if self.position_value.get(next_board_state) is None:
                #     value = 0
                # else :
                #     self.position_value(next_board_state)
                if value >= max_value:
                    max_value = value
                    choosen_move = p
        logging.info("Choosen move from the computer/ player one" + str(choosen_move))
        return choosen_move

    def available_position(self):
        # we need to store the availanle positon in the form of matrix
        # append the only position having the value 0 to the matrix, rest else is filled
        position = []
        for i in range(TOTAL_NUMBER_OF_ROWS):
            for k in range(TOTAL_NUMBER_OF_COLUMNS):
                if self.board[i, k] == 0:
                    position.append([i, k])
        return position

    def get_latest_board_values(self, board):
        latest_board = str(board.reshape(THE_BOARD))
        return latest_board

# Program execution
if __name__ == "__main__":
    # Train the player to play with each other
    player_one = PlayerTraining("playerOne")
    player_two = PlayerTraining("playerTwo")

    # Train the players to player to play with each other
    ready_to_play = TicTacToe(player_one, player_two)

    # Play the game
    ready_to_play.play_game(1)
