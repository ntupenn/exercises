"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - O - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""

# 1. find all buildings
# 2. BFS find distance d from each building to each space, save as distance[space][building] = d
# 3. for each point, check if len(distance[point]) == len(buildings), if so, sum up the distances

import sys
import collections

def shortestDistance(grid):
    if not grid or not grid[0]:
        return -1
    buildings = []
    rows, cols = len(grid), len(grid[0])
    for i in xrange(rows):
        for j in xrange(cols):
            if grid[i][j] == 1:
                buildings.append((i, j))
    distance = collections.defaultdict(lambda:collections.defaultdict(int))
    for r, c in buildings:
        queue = collections.deque([[r, c, 0]])
        visited = [[False] * cols for _ in xrange(rows)]
        while queue:
            i, j, d = queue.popleft()
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x, y = i + di, j + dj
                if x < 0 or x == rows or y < 0 or y == cols or visited[x][y] or grid[x][y] != 0:
                    continue
                visited[x][y] = True
                queue.append([x, y, d+1])
                distance[(x, y)][(i, j)] = d + 1
    d = sys.maxint
    for i in xrange(rows):
        for j in xrange(cols):
            if len(distance[(i, j)]) == len(buildings):
                d = min(d, sum(distance[(i, j)].values()))
    return d if d < sys.maxint else -1
