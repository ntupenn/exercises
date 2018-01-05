"""
Problem:
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.
"""

import collections

def groupStrings(strings):
    res = []
    mapping = collections.defaultdict(list)
    for s in strings:
        k = getKey(s)
        mapping[k].append(s)
    for k in mapping:
        res.append(sorted(mapping[k]))
    return res

def getKey(s):
    if not s:
        return ""
    key = []
    for c in s:
        key.append(chr((ord(c) - ord(s[0])) % 26))
    return "".join(key)

print groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
