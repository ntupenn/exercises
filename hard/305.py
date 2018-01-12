"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""

class UnionFind:
    def __init__(self, n):
        self.data = range(n)

    def find(self, x):
        if x == self.data[x]:
            return x
        y = self.find(self.data[x])
        self.data[x] = y
        return y

    def union(self, a, b):
        aa = self.find(a)
        bb = self.find(b)
        if aa != bb:
            self.data[aa] = bb

def numIslands2(m, n, positions):
    if m <= 0 or n <= 0:
        return []
    islands = UnionFind(m * n)
    check = set()
    res = []
    cnt = 0
    for x, y in positions:
        if x < 0 or x >= m or y < 0 or y >= m or (x, y) in check:
            continue
        check.add((x, y))
        cnt += 1
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            i, j = x + dx, y + dy
            if (i, j) in check:
                a = x * n + y
                b = i * n + j
                aa = islands.find(a)
                bb = islands.find(b)
                if aa == bb:
                    continue
                cnt -= 1
                islands.union(aa, bb)
        res.append(cnt)
    return res
