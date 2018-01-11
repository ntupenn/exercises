'''
Problem:
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
'''

def countPaintingWays(n, k):
    if n <= 0 or k <= 0:
        return 0
    if n > 2 and k < 2:
        return 0
    if n == 1:
        return k
    same = 0
    diff = k
    for _ in xrange(1, n):
        same, diff = diff, (diff + same) * (k-1)
    return same + diff

print countPaintingWays(10, 6)
