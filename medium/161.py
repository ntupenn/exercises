"""
An edit between two strings is one of the following changes:

Add a character
Delete a character
Change a character
Given two string s1 and s2, find if s1 can be converted to s2 with exactly one edit. Expected time complexity is O(m+n) where m and n are lengths of two strings.
"""

def isEditDistanceOne(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if len(s2) - len(s1) > 1:
        return False
    i1 = i2 = 0
    flag = False
    while i1 < len(s1):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            if flag:
                return False
            flag = True
            if len(s1) == len(s2):
                i1 += 1
            i2 += 1
    return flag or i2 < len(s2)
