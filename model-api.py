from flask import request
from flask import Flask
from flask_cors import CORS
import numpy as np
import pickle5 as pickle


app = Flask(__name__)
# allows front end to communicate with python
CORS(app)

# Initial flask app testing
@app.route('/')
def hello_world():
    return 'Welcome to the world of tic tac toe!'

# reshaping the board array to a numpy array
def get_latest_board_values(board):
    latest_board = str(board.reshape(3 * 3))
    return latest_board

def choose_move_two(position, current_board_state, symbol):
    # choosing move for the player two with symbol -1
    # The current board state has the type list and should follow the format : [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    # The current board state has the type should be numpy.ndArray: [[0. 0.0]
    #                                                                [1. 0.0]
    #                                                                [0. -1.0]]
    if np.random.uniform(0,1) <= 0:
        id = np.random.choice(len(position))
        choosen_move = position[id]
    else:
        # choose the move that maximizes to maximize the rewards
        max_value = -999
        for p in position:
            next_board = current_board_state.copy()
            next_board[p] = symbol
            next_board_state = get_latest_board_values(next_board)
            value = 0 if position_value_two.get(next_board_state) is None else position_value_two.get(next_board_state)
            if value >= max_value:
                max_value = value
                choosen_move = p

    return str(choosen_move)


# Choose the move based on the model
def choose_move(position, current_board_state, symbol):
    # The symbol format is "1"
    # The current board state has the type list and should follow the format : [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    # The current board state has the type should be numpy.ndArray: [[0. 0.0]
    #                                                                [1. 0.0]
    #                                                                [0. -1.0]]

    if np.random.uniform(0,1) <= 0:
        id = np.random.choice(len(position))
        choosen_move = position[id]
    else:
        # choose the move that maximizes to maximize the rewards
        max_value = -999
        for p in position:
            next_board = current_board_state.copy()
            next_board[p] = symbol
            next_board_state = get_latest_board_values(next_board)
            print(next_board_state)
            value = 0 if position_value.get(next_board_state) is None else position_value.get(next_board_state)
            if value >= max_value:
                max_value = value
                choosen_move = p
    print("choosen move: ", choosen_move)
    return str(choosen_move)

# Get the model moves from the api
@app.route('/api/move', methods=['POST', 'PUT', 'DELETE'])
def fetch():
    global position_value
    position_value =  {}
    global position_value_two
    position_value_two = {}

    # Load the binary value of model three
    file = open('final_model', 'rb')
    position_value = pickle.load(file)
    file.close()

    # Load the model of the file two
    file = open('final_model_two', 'rb')
    position_value_two = pickle.load(file)
    file.close()

    # Get the post values from JSON
    content_from_post_body = request.get_json()
    position = content_from_post_body['position']   #  or content_from_post_body.get('position')
    remaining_position = list(eval(position))
    current_board_state = content_from_post_body['current_board_state']  # content_from_post_body.get('current_board_state')
    current_board_state = np.array(list(eval(current_board_state))).astype(float)
    symbol = content_from_post_body['symbol']  # content_from_post_body.get('symbol')

    # Handling the position two
    if (symbol == 1):
        the_move = choose_move(remaining_position, current_board_state, symbol)
        return the_move
    else:
        the_move = choose_move_two(remaining_position, current_board_state, symbol)
        return the_move

