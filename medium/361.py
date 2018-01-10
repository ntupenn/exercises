"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""

def maxKilledEnemies(grid):
    if not grid or not grid[0]:
        return 0
    cnt = 0
    row = 0
    cols = [0] * len(grid[0])
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if j == 0 or grid[i][j-1] == "W":
                row = 0
                jj = j
                while jj < len(grid[0]) and grid[i][jj] != "W":
                    row += 1 if grid[i][jj] == "E" else 0
                    jj += 1
            if i == 0 or grid[i-1][j] == "W":
                cols[j] = 0
                ii = i
                while ii < len(grid) and grid[ii][j] != "W":
                    cols[j] += 1 if grid[ii][j] == "E" else 0
                    ii += 1
            if grid[i][j] == "0":
                cnt = max(cnt, row + cols[j])
    return cnt

grid = [["0", "E", "0", "0",],
        ["E", "0", "W", "E",],
        ["0", "E", "0", "0",]]

print maxKilledEnemies(grid)
