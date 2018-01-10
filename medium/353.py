"""
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.
The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.
Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.
When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
Example:
Given width = 3, height = 2, and food = [[1,2],[0,1]].
Snake snake = new Snake(width, height, food);
Initially the snake appears at position (0,0) and the food at (1,2).
|S| | |
| | |F|
snake.move("R"); -> Returns 0
| |S| |
| | |F|
snake.move("D"); -> Returns 0
| | | |
| |S|F|
snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
| |F| |
| |S|S|
snake.move("U"); -> Returns 1
| |F|S|
| | |S|
snake.move("L"); -> Returns 2 (Snake eats the second food)
| |S|S|
| | |S|
snake.move("U"); -> Returns -1 (Game over because snake collides with border)
"""

import collections

class SnakeGame:
    def __init__(self, w, h, food):
        self.w, self.h, self.food = w, h, food
        self.queue = collections.deque()
        self.queue.append((0, 0))
        self.snake = set()
        self.snake.add((0, 0))
        self.directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
        self.idx = 0

    def move(self, direction):
        if direction not in self.directions:
            return len(self.snake)
        head = self.queue[0]
        tail = self.queue.pop()
        self.snake.remove(tuple(tail))
        dx, dy = self.directions[direction]
        x, y = head[0] + dx, head[1] + dy
        if x < 0 or x == self.h or y < 0 or y == self.w or (x, y) in self.snake:
            return -1
        self.snake.add((x, y))
        self.queue.appendleft((x, y))
        if self.idx < len(self.food) and [x, y] == self.food[self.idx]:
            self.snake.add(tail)
            self.queue.append(tail)
            self.idx += 1
        return self.idx

    def printSnake(self):
        self.board = [[" "] * self.w for _ in xrange(self.h)]
        for x, y in self.snake:
            self.board[x][y] = "S"
        if self.idx < len(self.food):
            x, y = self.food[self.idx]
            self.board[x][y] = "F"
        for i in xrange(self.h):
            print "|".join([""] + self.board[i] + [""])

# Test
game = SnakeGame(3, 2, [[1,2],[0,1]])
game.printSnake()
print game.move("R")
game.printSnake()
print game.move("D")
game.printSnake()
print game.move("R")
game.printSnake()
print game.move("U")
game.printSnake()
print game.move("L")
game.printSnake()
print game.move("U")
game.printSnake()
