"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.
"""

def wordPatternMatch(pattern, str):
    if len(str) < len(pattern):
        return False
    return helper(pattern, str, {}, {})

def helper(pattern, s, check1, check2):
    if not pattern and not s:
        return True
    if not pattern or not s:
        return False
    if pattern[0] in check1:
        val = check1[pattern[0]]
        if val != s[:len(val)]:
            return False
        return helper(pattern[1:], s[len(val):], check1, check2)
    for size in xrange(1, len(s) + 1):
        if s[:size] in check2:
            continue
        check1[pattern[0]] = s[:size]
        check2[s[:size]] = pattern[0]
        res = helper(pattern[1:], s[size:], check1, check2)
        del check1[pattern[0]]
        del check2[s[:size]]
        if res:
            return True
    return False
