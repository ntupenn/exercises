"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

Example 1:
11000
10000
00001
00011
Given the above grid map, return 1.

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.

Example 2:
11100
10001
01001
01110
Given the above grid map, return 2.

Here are the two distinct islands:
111
1
and
1
1
Notice that:


111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.

Note: The length of each dimension in the given grid does not exceed 50.
"""

import collections

def numDistinctIslandsII(grid):
    if not grid or not grid[0]:
        return 0
    check = set()
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == 1:
                shape = islandHelperII(grid, i, j)
                flag = True
                for _ in xrange(4):
                    shape = rotateII(shape)
                    if shape in check:
                        flag = False
                        break
                if not flag:
                    continue
                shape = mirror(shape)
                for _ in xrange(4):
                    shape = rotateII(shape)
                    if shape in check:
                        flag = False
                        break
                if flag:
                    check.add(shape)
    return len(check)

def islandHelperII(grid, i, j):
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

def rotateII(shape):
    maxx = minx = 0
    for x, _ in shape:
        maxx = max(maxx, x)
        minx = min(minx, x)
    sumx = maxx + minx
    new_shape = []
    for x, y in shape:
        new_shape.append((y, sumx-x))
    new_shape.sort(key=lambda x:(x[0], x[1]))
    for i in xrange(len(new_shape)-1, -1, -1):
        new_shape[i] = (new_shape[i][0] - new_shape[0][0], new_shape[i][1] - new_shape[0][1])
    return tuple(new_shape)

def mirror(shape):
    maxy = miny = 0
    for _, y in shape:
        maxy = max(maxy, y)
        miny = min(miny, y)
    sumy = miny + maxy
    new_shape = []
    for x, y in shape:
        new_shape.append((x, sumy-y))
    return tuple(new_shape)

# def printHelper(shape):
#     maxx = minx = maxy = miny = 0
#     for x, y in shape:
#         maxx = max(maxx, x)
#         minx = min(minx, x)
#         maxy = max(maxy, y)
#         miny = min(miny, y)
#     rows = maxx - minx + 1
#     cols = maxy - miny + 1
#     matrix = [["."] * cols for _ in xrange(rows)]
#     for x, y in shape:
#         matrix[x-minx][y-miny] = "*"
#     for row in matrix:
#         print row


grid = [[1,0,0,1,0,0,0,0,0,1,0,1,0,0,1],
        [1,0,1,0,0,1,1,1,0,1,1,0,1,0,0],
        [0,0,0,0,0,1,0,1,0,0,0,1,0,1,0],
        [1,0,0,0,1,1,1,0,1,0,0,1,1,0,0],
        [0,1,0,1,1,0,0,1,1,0,1,0,1,0,1],
        [1,0,1,0,0,0,1,0,0,1,1,0,0,1,0],
        [1,0,0,1,0,1,1,1,1,0,1,1,1,1,0],
        [0,0,1,1,0,0,1,0,1,1,0,1,0,0,1],
        [0,0,1,0,0,0,0,1,0,0,1,0,0,0,0],
        [1,1,0,0,1,1,1,0,1,1,0,1,0,0,1]]

print numDistinctIslandsII(grid)
