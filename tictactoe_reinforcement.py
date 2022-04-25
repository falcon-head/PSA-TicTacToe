"""
Author: Shrikrishna Joisa
Creted on: 2022-06-04
Last Updated on: 2022-12-04
"""

import numpy as np
import logging
import pickle5 as pickle
from tqdm import tqdm
import datetime
import matplotlib.pyplot as plt

# Tic toe using reinforcement learning (Q-learning)
# We will use feed forward network to approximate the Q-function and use the epsilon-greedy policy to select the next action.
# Greedy policy uses the prior knowledge and the current state to select the next action.

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
        and initial board valeu is zero, player one move value is 1 and player two move value is -1
    """

    def __init__(self, player_one, player_two):
        self.board = np.zeros((TOTAL_NUMBER_OF_ROWS, TOTAL_NUMBER_OF_COLUMNS))
        self.player_one = player_one
        self.player_two = player_two
        self.game_has_ended = False
        self.winner = None
        self.latest_board_state = None
        self.player_symbol = 1  # when the player takes the first move, the symbol is 1
        self.player_one_wins = 0
        self.player_two_wins = 0
        self.draws  = 0
        self.barGraphList = []

    def play_game(self, number_of_rounds):
        for i in tqdm(range(number_of_rounds)):
            while not self.game_has_ended:
                # Player one moves
                # Get the available position, based on the available position, select the moves with the coorect player symbol
                # update the state of the board with the selected move
                # Add the state to the list of states values
                # Check whether the user has won the game or not based on that reward the agent
                position = self.available_position()
                logging.info("The available positions are" + str(position))
                player_one_choose_move = self.player_one.choose_move(position, self.board, self.player_symbol)
                logging.info("Player one choose the move" + str(player_one_choose_move))
                self.update_board_state(player_one_choose_move)
                new_board_state = self.get_latest_board_values()
                logging.info("The board values" + str(new_board_state))
                self.player_one.add_state(new_board_state)
                # Check if the game has ended or not
                # award the reward to the agent
                # reset the player states and board state if it's a win or a draw
                # if the game has ended, break the loop
                win = self.check_win()
                if win is not None:
                    self.award_reward()
                    self.player_one.reset_state()
                    self.player_two.reset_state()
                    self.board_reset()
                    break
                else:
                    # Check if the game has ended or not
                    # award the reward to the agent
                    # reset the player states and board state if it's a win or a draw
                    # if the game has ended, then break the loop
                    position = self.available_position()
                    logging.info("The available positions are" + str(position))
                    player_two_choose_move = self.player_two.choose_move(position, self.board, self.player_symbol)
                    logging.info("Player two choose the move" + str(player_two_choose_move))
                    self.update_board_state(player_two_choose_move)
                    new_board_state = self.get_latest_board_values()
                    self.player_two.add_state(new_board_state)

                    win = self.check_win()
                    if win is not None:
                        self.award_reward()
                        self.player_one.reset_state()
                        self.player_two.reset_state()
                        self.board_reset()
                        break

        print(self.player_one_wins)
        print(self.player_two_wins)
        print(self.draws)
        self.barGraphList.append(self.player_one_wins)
        self.barGraphList.append(self.player_two_wins)
        self.barGraphList.append(self.draws)
        # self.plot_bar_graph()

    """
    Check for the available position in the board and append it to position
    returns : position matrix
    """

    def plot_bar_graph(self):
        # create the bar graph figure
        fig = plt.figure(figsize=  (10,5))
        items = ["Player One", "Player Two", "Draws"]
        plt.bar(items, self.barGraphList)
        plt.xlabel("Players")
        plt.ylabel("Number of Wins")
        plt.title("Win Comparison")
        plt.savefig("win_comparison.png")

    # def plot_show_rewards_graph(self):
    #     fig = plt.figure(figsize=  (10, 5))
    #     plt.plot(PLAYER_GAME_NUMBER, PLAYER_ONE_REWARDS, label = "Player One")
    #     plt.plot(PLAYER_GAME_NUMBER, PLAYER_TWO_REWARDS, label = "Player Two")
    #     plt.xlabel("Games")
    #     plt.ylabel("Rewards")
    #     plt.title("Rewards Comparison")
    #     plt.legend()
    #     plt.savefig("rewards_comparison.png")
    #     plt.show()

    def available_position(self):
        # we need to store the availanle positon in the form of matrix
        # append the only position having the value 0 to the matrix, rest else is filled
        position = []
        for i in range(TOTAL_NUMBER_OF_ROWS):
            for k in range(TOTAL_NUMBER_OF_COLUMNS):
                if self.board[i, k] == 0:
                    position.append((i, k))
        return position


    """
    Update the board position based on the player move
    If player one is playing his symbol is 1
    If player two is playing his symbol is 2
    """
    def update_board_state(self, position):
        self.board[position] = self.player_symbol
        if(self.player_symbol == 1):
            self.player_symbol = -1
        else:
            self.player_symbol = 1

    """
    Get the latest board value
    """
    def get_latest_board_values(self):
        latest_board = str(self.board.reshape(THE_BOARD))
        return latest_board

    """
    Function which is used to check the winning condition of the tictactoe
    Here we will consider row winning condition, if the player one row sum is == 3, then the player one has won the mtach
    if the player two row sum is == -3, then the player two has won the match
    Add diagonal condition as well to check for the win, If the diagonal is complete with single symbol then the player wills secure the win
    Along with the tie condition as well
    """
    def check_win(self):
        # Check for the row sum at first
        for i in range(TOTAL_NUMBER_OF_ROWS):
            # Player one row sum
            if sum(self.board[i, :]) == 3:
                self.game_has_ended = True
                logging.info("Player one has won the match")
                return 1

            # Player two row sum
            if sum(self.board[i, :]) == -3:
                self.game_has_ended = True
                logging.info("Player two has won the match")
                return -1

        # Check for the column sum
        for j in range(TOTAL_NUMBER_OF_COLUMNS):
            # Player one column sum
            if sum(self.board[:, j]) == 3:
                self.game_has_ended = True
                logging.info("Player one has won the match")
                return 1

            # Player two column sum
            if sum(self.board[:, j]) == -3:
                self.game_has_ended = True
                logging.info("Player two has won the match")
                return -1

        # Check for the diagonal sum
        diagonal_one_sum = sum([self.board[i,i] for i in range(TOTAL_NUMBER_OF_COLUMNS)])
        diagonal_two_sum = sum([self.board[i, TOTAL_NUMBER_OF_COLUMNS - i - 1] for i in range(TOTAL_NUMBER_OF_COLUMNS)])
        diagonal_sum = max(abs(diagonal_one_sum), abs(diagonal_two_sum))
        # Calculate the two diagonal sum
        # once you calculate check if the diagonal sum is 3 or -3
        # if the diagonal sum is 3 then the player one has won the mtach else palayer two has won the match

        if(diagonal_sum == 3):
            self.game_has_ended = True
            if diagonal_one_sum == 3 or diagonal_two_sum == 3:
                logging.info("Player one has won the match")
                return 1
            else:
                logging.info("Player one has won the match")
                return -1

        # No position remaining, then it's a tie
        if len(self.available_position()) == 0:
            self.game_has_ended = True
            logging.info("Match is a tie")
            return 0

        self.game_has_ended = False
        return None

    # agent reward mechanism by backpropagation
    # if the player one winsm, then reward the player one with 1 and player two with 0
    # if the player two wins, then reward the player two with 1  and player one with 0
    # if the game is a draw, then reward both player with 0.5
    def award_reward(self):
        result = self.check_win()
        if result == 1:
            logging.info("Rewarded player one with 1")
            self.player_one_wins +=1
            self.player_one.reward(1)
            self.player_two.reward(0)
        elif result == -1:
            logging.info("Rewarded player two with 1")
            self.player_two_wins += 1
            self.player_one.reward(0)
            self.player_two.reward(1)
        else:
            logging.info("Rewarded both player with 0.5")
            self.draws += 1
            self.player_one.reward(0.2)
            self.player_two.reward(0.5)

    """
        Reset the entire board state, symbol & the latest_board_state
    """
    def board_reset(self):
        self.board = np.zeros((TOTAL_NUMBER_OF_ROWS, TOTAL_NUMBER_OF_COLUMNS))
        self.game_has_ended = False
        self.player_symbol = 1
        self.latest_board_state = None
        logging.info("The board has been reset")

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
        self.position_state = []
        self.learning_rate = 0.2
        self.discount_rate = 0.8
        self.exploratory_move = 0.3  # make a random move to experience all the states present in the game
        self.greedy_move = 0.7 # To maximize the rewards
        self.position_value = {} # state position value dictionary
        self.reward_list = []

    """
        Uniformly choose a random move, an exploratory move where the player takes the move randomly to go through all the possiblile state
        The data is uniformly distributed with the help of uniform method & compared with the expolatory move
        returns: move to be choosen
    """
    def choose_move(self, position, current_board_state, symbol):
        # make a random move
        # get the random index from the position
        # get the the particular index from the availabel positon using position[index]
        if np.random.uniform(0,1) <= self.exploratory_move:
            id = np.random.choice(len(position))
            choosen_move = position[id]
        else:
            # choose the move that maximizes to maximize the rewards
            max_value = -999
            for p in position:
                next_board = current_board_state.copy()
                next_board[p] = symbol
                next_board_state = self.get_latest_board_values(next_board)
                value = 0 if self.position_value.get(next_board_state) is None else self.position_value.get(next_board_state)
                if value >= max_value:
                    max_value = value
                    choosen_move = p
        logging.info("Choosen move from the computer/ player one" + str(choosen_move))
        return choosen_move

    """
    Find the available positions on the board
    """

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
    Get the latest board value
    """
    def get_latest_board_values(self, board):
        latest_board = str(board.reshape(THE_BOARD))
        return latest_board

    """
    Append a list to a state
    """
    def add_state(self, state):
        self.position_state.append(state)

    """
    backpropagate and update the state in the Q-learning algorithm
    """
    def reward(self, reward):
        for state in reversed(self.position_state):
            if self.position_value.get(state) is None:
                self.position_value[state] = 0
            # Q learning formula
            self.position_value[state] += self.learning_rate * (self.discount_rate + reward - self.position_value[state])
            reward = self.position_value[state]

    """
    reset the states of the player and board
    """
    def reset_state(self):
        self.position_state = []

    """
    Save the model using pickle for the player to integrate with the other apps
    """
    def save_model(self):
        model_pickle_file = open("model_" + str(self.player_name) + "_" + str(datetime.datetime.now()), "wb")
        pickle.dump(self.position_value, model_pickle_file)
        model_pickle_file.close()


# Program execution
if __name__ == "__main__":
    # Train the player to play with each other
    player_one = PlayerTraining("player_one")
    player_two = PlayerTraining("player_two")

    # Train the players to player to play with each other
    ready_to_play = TicTacToe(player_one, player_two)
    logging.info("The training has started")
    # Play the game
    ready_to_play.play_game(1)
    # Save the model
    # player_one.save_model()
    # player_two.save_model()
