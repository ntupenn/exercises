"""
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:
Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.

Note:
All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""

# 1. find occurrence of first char in t in s
# 2. loop through to find next char in t, mark it as starting point idx
# 3. check if starting point to idx is no shorter than t

def minWindow(s, t):
    if len(t) > len(s):
        return ""
    ls, lt = len(s), len(t)
    curr = [-1] * ls
    for i in xrange(ls):
        if s[i] == t[0]:
            curr[i] = i
    for j in xrange(1, lt):
        prev = curr
        curr = [-1] * ls
        start = -1
        for i in xrange(ls):
            # note the sequence of two if here
            if s[i] == t[j] and start >= 0:
                curr[i] = start
            if prev[i] >= 0:
                start = prev[i]
    res = ""
    for i in xrange(ls):
        if curr[i] >= 0:
            length = i - curr[i] + 1
            if not res or length < len(res):
                res = s[curr[i]:i+1]
    return res
