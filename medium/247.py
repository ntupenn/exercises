"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
"""

def findStrobogrammatic(n):
    mapping = {"0": "0", "1": "1", "6" : "9", "8": "8", "9": "6"}
    return helper(n, n, mapping)

def helper(n, m, mapping):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "8"]
    tmp = helper(n-2, n, mapping)
    res = []
    for t in tmp:
        for prefix in mapping:
            if n == m and prefix == "0":
                continue
            res.append(prefix + t + mapping[prefix])
    return res

print findStrobogrammatic(4)
