"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 <= m <= n <= 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
"""

def countPatterns(m, n):
    if m < 1 or n < 1 or m > 9 or n > 9 or m > n:
        return 0
    check = [[0] * 10 for _ in xrange(10)]
    through = [(1, 3, 2), (1, 7, 4), (1, 9, 5), (2, 8, 5), (3, 7, 5), (3, 9, 6), (4, 6, 5), (7, 9, 8)]
    for a, b, c in through:
        check[a][b] = c
        check[b][a] = c
    used = [False] * 10 # not use 0
    used[0] = True
    #      symmetric corners * 4                 symmetric sides * 4                   center
    return helper(m, n, used, check, 1, 1) * 4 + helper(m, n, used, check, 2, 1) * 4 + helper(m, n, used, check, 5, 1)

def helper(m, n, used, check, point, size):
    count = 0
    if size >= m:
        count += 1
    size += 1
    if size > n:
        return count
    used[point] = True
    for next_point in xrange(1, 10):
        if not used[next_point] and used[check[point][next_point]]:
            count += helper(m, n, used, check, next_point, size)
    used[point] = False
    return count

print countPatterns(1, 9)
