"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
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

def count(n, edges):
    graph = UnionFind(n)
    for a, b in edges:
        if a < 0 or a >= n or b < 0 or b >= n:
            continue
        graph.union(a, b)
    count = 0
    for i in xrange(n):
        if i == graph.find(i):
            count += 1
    return count
