'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

import collections

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.sum = 0
        self.queue = collections.deque()

    def next(self, val):
        if len(self.queue) == self.size:
            tmp = self.queue.popleft()
            self.sum -= tmp
        self.sum += val
        self.queue.append(val)
        return 1.0 * self.sum / len(self.queue)
