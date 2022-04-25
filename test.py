import numpy as np
import pandas as pd

# Data testing
board_positions = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
board =  np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]).astype(float)
board_one =  np.array([[0, 0, 0], [0, 0, 0], [0, 0, -1]]).astype(int)
print(board_one)
print(type(board))
print(type(board_positions))

def another_function(board_one):
    position = []
    for i in range(3):
        for k in range(3):
            if board_one[i, k] == 0:
                position.append((i, k))
    return position

answer = another_function(board_one)

board_reshape = board_one.reshape(3 * 3)
print(board_reshape)


