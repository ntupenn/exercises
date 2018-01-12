"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10

Note:

The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 < row2 and col1 < col2.
"""

class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        if not matrix or not matrix[0]:
            self.rows = matrix
        else:
            self.rows = [[matrix[i][j]for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
            for i in xrange(len(matrix)):
                for j in xrange(1, len(matrix[0])):
                    self.rows[i][j] += self.rows[i][j-1]

    def update(self, i, j, val):
        if i < 0 or i >= len(self.matrix) or j < 0 or j >= len(self.matrix[0]):
            return
        diff = val - self.matrix[i][j]
        self.matrix[i][j] = val
        for jj in xrange(j, len(matrix[0])):
            self.rows[i][jj] += diff

    def sumRegion(self, i1, j1, i2, j2):
        if i1 < 0 or i2 < 0 or j1 < 0 or j2 < 0 or i1 >= len(self.matrix) or i2 >= len(self.matrix) or j1 >= len(self.matrix[0]) or j2 >= len(self.matrix[0]):
            return 0
        return self.getSum(i2, j2) - self.getSum(i1-1, j2) - self.getSum(i2, j1-1) + self.getSum(i1-1, j1-1)

    def getSum(self, i, j):
        if i < 0 or j < 0:
            return 0
        res = 0
        for ii in xrange(i+1):
            res += self.rows[ii][j]
        return res
