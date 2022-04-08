import numpy as np
import pandas as pd



class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.player = 1
        self.winner = None
        self.ended = False
        self.num_states = 3 ** 9

    def move(self, row, col):
        self.board[row, col] = self.player
        self.flip_player()
        self.check_win()

    def flip_player(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1

    def check_win(self):
        for player in (1, 2):
            # Check for horizontal wins
            if np.all(self.board == player):
                self.winner = player
                self.ended = True
            # Check for vertical wins
            if np.all(self.board.T == player):
                self.winner = player
                self.ended = True
            # Check for diagonal wins
            if np.all(np.diag(self.board) == player):
                self.winner = player
                self.ended = True
            if np.all(np.diag(np.fliplr(self.board)) == player):
                self.winner = player
                self.ended = True

        # Check for draw
        if np.all(self.board != 0):
            self.winner = 0
            self.ended = True

    def draw_board(self):
        for i in range(3):
            print("-------------")
            out = "| "
            for j in range(3):
                if self.board[i, j] == 1:
                    token = "X"
                if self.board[i, j] == 2:
                    token = "O"
                if self.board[i, j] == 0:
                    token = " "
                out += token + " | "
            print(out)

    def reset(self):
        self.board = np.zeros((3, 3))
        self.player = 1
        self.winner = None
        self.ended = False


if __name__ == "__main__":
    game = TicTacToe()
    game.draw_board()
    while not game.ended:
        if game.player == 1:
            game.move(int(input("Player 1: Enter row: ")), int(input("Player 1: Enter col: ")))
        else:
            game.move(int(input("Player 2: Enter row: ")), int(input("Player 2: Enter col: ")))
        game.draw_board()
    if game.winner == 1:
        print("Player 1 won!")
    elif game.winner == 2:
        print("Player 2 won!")
    else:
        print("Draw!")