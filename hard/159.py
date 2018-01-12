"""
Description:
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
For example, Given s = "eceba",
T is "ece" which its length is 3.
"""

# O(1) space, since check has at most 3 items in

def lengthOfLongestSubstringWithTwoDistinctChar(s):
    if len(s) < 3:
        return len(s)
    check = {}
    start = end = res = 0
    while end < len(s):
        check[s[end]] = check.get(s[end], 0) + 1
        while len(check) > 2:
            check[s[start]] -= 1
            if check[s[start]] == 0:
                del check[s[start]]
            start += 1
        end += 1
        res = max(res, end - start)
    return res
