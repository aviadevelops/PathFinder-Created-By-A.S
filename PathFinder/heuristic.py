# Copyright - all rights reserved to A.S.

import random


class Heuristic:
    def __init__(self, board_size):
        self.board_size = board_size
        self.arr = [[0] * self.board_size for i in range(self.board_size)]
        self.board = [[0] * self.board_size for i in range(self.board_size)]
        self.profit = 0

    def randomize_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.board[i][j] = random.randint(1, 1000)

    def fill_array(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if i == 0 and j == 0:
                    self.arr[0][0] = self.board[0][0]
                elif i == 0:
                    self.arr[i][j] = self.board[i][j] + self.arr[i][j - 1]
                elif j == 0:
                    self.arr[i][j] = self.board[i][j] + self.arr[i - 1][j]
                else:
                    self.arr[i][j] = self.board[i][j] + max(self.arr[i][j - 1], self.arr[i - 1][j],
                                                            self.arr[i - 1][j - 1])
        self.profit = self.arr[self.board_size - 1][self.board_size - 1]
        return self.arr[self.board_size - 1][self.board_size - 1]

    def recover_path(self):
        path_stack = []
        i = self.board_size - 1
        j = self.board_size - 1
        path_stack.append((i, j))

        while i != 0 or j != 0:
            if self.arr[i][j] == self.board[i][j] + self.arr[i][j - 1]:
                path_stack.append((i, j - 1))
                j -= 1
            elif self.arr[i][j] == self.board[i][j] + self.arr[i - 1][j]:
                path_stack.append((i - 1, j))
                i -= 1
            else:
                path_stack.append((i - 1, j - 1))
                i -= 1
                j -= 1
        return path_stack

    def calculate_max_profit_path(self):
        self.randomize_board()
        print(self.board)
        self.fill_array()
        print(self.arr)
        print(self.recover_path())
