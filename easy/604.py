'''
Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.
The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.
next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
hasNext() - Judge whether there is any letter needs to be uncompressed.
Note:
Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
'''

class StringIterator:
    def __init__(self, s):
        self.chars = []
        self.cnts = []
        num = 0
        char = ''
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if num > 0:
                    self.chars.append(char)
                    self.cnts.append(num)
                char = c
                num = 0
        self.chars.append(char)
        self.cnts.append(num)
        self.idx = 0
        self.cnt = 0

    def hasNext(self):
        return self.idx < len(self.chars)

    def next(self):
        if not self.hasNext():
            return " "
        char = self.chars[self.idx]
        self.cnt += 1
        if self.cnt == self.cnts[self.idx]:
            self.idx += 1
            self.cnt = 0
        return char

iterator = StringIterator("L1e2t1C1o1d1e1");
print iterator.next();    # // return 'L'
print iterator.next();    # // return 'e'
print iterator.next();    # // return 'e'
print iterator.next();    # // return 't'
print iterator.next();    # // return 'C'
print iterator.next();    # // return 'o'
print iterator.next();    # // return 'd'
print iterator.hasNext(); # // return true
print iterator.next();    # // return 'e'
print iterator.hasNext(); # // return false
print iterator.next();    # // return ' '
