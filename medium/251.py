"""
Implement an iterator to flatten a 2d vector.
For example,
Given 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
Hint:
How many variables do you need to keep track?
Two variables is all you need. Try with x and y.
Beware of empty rows. It could be the first few rows.
To write correct code, think about the invariant to maintain. What is it?
The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
Not sure? Think about how you would implement hasNext(). Which is more complex?
Common logic in two different places should be refactored into a common method.
"""

class Vector2D:
    def __init__(self, vec2d):
        self.row = 0
        self.col = 0
        self.data = []
        for vec in vec2d:
            if vec:
                self.data.append(vec)

    def next(self):
        val = self.data[self.row][self.col]
        self.col += 1
        if self.col == len(self.data[self.row]):
            self.row += 1
            self.col = 0
        return val

    def hasNext(self):
        return self.row < len(self.data)

vec2d = [
  [1,2],
  [3],
  [4,5,6],
  [],
  [7]
]

v = Vector2D(vec2d)
while v.hasNext():
    print v.next()
