from flask import request
from flask import Flask
import pandas as pd
import numpy as np
import pickle5 as pickle


app = Flask(__name__)

# to store the pickle state
position_value = {}

# Initial flask app testing
@app.route('/')
def hello_world():
    return 'Welcome to the world of tic tac toe!'

# reshaping the board array to a numpy array
def get_latest_board_values(board):
    latest_board = str(board.reshape(3 * 3))
    return latest_board

# Choose the move based on the model
def choose_move(position, current_board_state, symbol):
    # The symbol format is "1" or "-1"
    # The current board state has the type list and should follow the format : [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    # The current board state has the type should be numpy.ndArray: [[0. 0.0]
    #                                                                [1. 0.0]
    #                                                                [0. -1.0]]
    if np.random.uniform(0,1) <= 0:
        id = np.random.choice(len(position))
        choosen_move = position[id]
        print("if")
    else:
        # choose the move that maximizes to maximize the rewards
        print("else")
        max_value = -999
        for p in position:
            next_board = current_board_state.copy()
            next_board[p] = symbol
            next_board_state = get_latest_board_values(next_board)
            value = 0 if position_value.get(next_board_state) is None else position_value.get(next_board_state)
            if value >= max_value:
                max_value = value
                choosen_move = p
                print(choosen_move)
    print("choosen move: ", choosen_move)
    return str(choosen_move)

# Get the model moves from the api
@app.route('/api/move', methods=['POSt', 'PUT', 'DELETE'])
def fetch():
    file = open('final_model', 'rb')
    position_value = pickle.load(file)
    file.close

    # Get the post values from JSON
    content_from_post_body = request.get_json()
    position = content_from_post_body['position']   #  or content_from_post_body.get('position')
    remaining_position = list(eval(position))
    current_board_state = content_from_post_body['current_board_state']  # content_from_post_body.get('current_board_state')
    current_board_state = np.array(list(eval(current_board_state)))
    symbol = content_from_post_body['symbol']  # content_from_post_body.get('symbol')


    the_move = choose_move(remaining_position, current_board_state, symbol)
    return the_move