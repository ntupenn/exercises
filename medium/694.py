"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:

11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:

11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:

11
1
and

 1
11
are considered different island shapes, because we do not consider reflection / rotation.

Note: The length of each dimension in the given grid does not exceed 50.
"""

import collections

def numDistinctIslands(grid):
    if not grid or not grid[0]:
        return 0
    check = set()
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == 1:
                shape = islandHelper(grid, i, j)
                check.add(shape)
    return len(check)

def islandHelper(grid, i, j):
    queue = collections.deque()
    queue.append((i, j))
    shape = []
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 0:
            continue
        shape.append((x-i, y-j))
        grid[x][y] = 0
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r, c = x+dx, y+dy
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1:
                queue.append((r, c))
    return tuple(shape)

grid = [[1,1,0,1,1],
        [1,0,0,0,0],
        [0,0,0,0,1],
        [1,1,0,1,1]]
print numDistinctIslands(grid)
