"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?
"""

def reverseWords(s):
    s = list(s)
    start = 0
    for end in xrange(len(s)):
        if s[end] == " ":
            reverse(s, start, end-1)
            start = end+1
    reverse(s, start, len(s)-1)
    reverse(s, 0, len(s)-1)
    return "".join(s)

def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
