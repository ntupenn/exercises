"""
Problem:
Given two 1d vectors, implement an iterator to return their elements alternately.
For example, given two 1d vectors:
v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
"""

class ZigzagIterator:
    def __init__(self, v1, v2):
        self.v1, self.v2 = v1, v2
        self.idx1 = self.idx2 = 0
        self.flag = True

    def hasNext(self):
        return self.idx1 < len(self.v1) or self.idx2 < len(self.v2)

    def next(self):
        if (self.flag and self.idx1 < len(self.v1)) or self.idx2 == len(self.v2):
            val = self.v1[self.idx1]
            self.idx1 += 1
        else:
            val = self.v2[self.idx2]
            self.idx2 += 1
        self.flag = not self.flag
        return val
