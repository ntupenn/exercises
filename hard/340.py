"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.
For example, Given s = "eceba" and k = 2,
T is "ece" which its length is 3.
"""

def longestSubstring(s, k):
    if len(s) <= k:
        return s
    check = {}
    start = 0
    res = k
    for end in xrange(len(s)):
        check[s[end]] = check.get(s[end], 0) + 1
        while len(check) > k:
            check[s[start]] -= 1
            if check[s[start]] == 0:
                del check[s[start]]
            start += 1
        res = max(res, end - start + 1)
    return res
