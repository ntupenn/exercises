"""
Design a Phone Directory which supports the following operations:
get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:
// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);
// It can return any available phone number. Here we assume it returns 0.
directory.get();
// Assume it returns 1.
directory.get();
// The number 2 is available, so return true.
directory.check(2);
// It returns 2, the only number that is left.
directory.get();
// The number 2 is no longer available, so return false.
directory.check(2);
// Release number 2 back to the pool.
directory.release(2);
// Number 2 is available again, return true.
directory.check(2);
"""

class PhoneDirectory:
    def __init__(self, n):
        self.nums = range(n)
        self.used = [False] * n
        self.n = n

    def get(self):
        if self.n == 0:
            return -1
        self.n -= 1
        num = self.nums[self.n]
        self.used[num] = True
        return num

    def check(self, num):
        return not self.used[num]

    def release(self, num):
        if self.used[num]:
            self.used[num] = False
            self.nums[self.n] = num
            self.n += 1
