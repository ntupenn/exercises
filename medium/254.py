"""
Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:
Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
You may assume that n is always positive.
Factors should be greater than 1 and less than n.

Examples:
input: 1
output:
[]

input: 37
output:
[]

input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""

def getFactors(num):
    if num <= 1:
        return []
    factors = []
    for i in xrange(2, num / 2 + 1):
        if num % i == 0:
            factors.append(i)
    res = []
    helper(res, factors, 0, num, [])
    return res

def helper(res, factors, idx, num, tmp):
    if num == 1:
        res.append(tmp[:])
        return
    for i in xrange(idx, len(factors)):
        if factors[i] > num:
            break
        if num % factors[i] == 0:
            tmp.append(factors[i])
            helper(res, factors, i, num / factors[i], tmp)
            tmp.pop()
