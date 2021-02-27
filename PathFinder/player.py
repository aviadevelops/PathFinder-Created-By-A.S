# Copyright - all rights reserved to A.S.

class Player:
    def __init__(self):
        self.current_position = (0, 0)
        self.profit = 0

    def is_legal(self, new_position):
        i = new_position[0]
        j = new_position[1]
        k = self.current_position[0]
        r = self.current_position[1]
        if (i - 1 == k and j == r) or (i == k and j - 1 == r) or (i - 1 == k and j - 1 == r):
            return True
        return False

    def move(self, new_position, board):
        self.current_position = new_position
        self.profit += board[new_position[0]][new_position[1]]

    def current_square(self, pos, size):
        for i in range(size):
            for j in range(size):
                if i * 800 // size < pos[0] < (i + 1) * 800 // size and j * 600 // size < pos[1] < (
                        j + 1) * 600 // size:
                    return j, i
