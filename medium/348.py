"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
"""

class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = [0, 0]
        self.check = set()
        self.user = 1 # assume player 1 and player 2

    def move(self, i, j, player):
        if player != self.user or player not in (1, 2):
            return 0
        if (i, j) in self.check:
            return 0
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return 0
        self.check.add((i, j))
        point = 1 if player == 1 else -1
        target = point * self.n
        self.rows[i] += point
        if self.rows[i] == target:
            return player
        self.cols[j] += point
        if self.cols[j] == target:
            return player
        if i == j:
            self.diagonal[0] += point
            if self.diagonal[0] == target:
                return player
        if i + j == self.n - 1:
            self.diagonal[1] += point
            if self.diagonal[1] == target:
                return player
        return 0
