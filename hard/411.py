"""
A string such as "word" contains the following abbreviations:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.
Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.
Note:
In the case of multiple answers as shown in the second example below, you may return any one of them.
Assume length of target string = m, and dictionary size = n. You may assume that m <= 21, n <= 1000, and log2(n) + m <= 20.

Examples:
"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")
"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
"""

def minAbbreviation(target, dictionary):
    check = [word for word in dictionary if len(word) == len(target)]
    if not check:
        return len(target)
    abbrs = getAbbreviation(target)
    abbrs.sort(key=lambda x:len(x))
    for abbr in abbrs:
        flag = True
        for word in check:
            if isValidAbbreviation(abbr, word):
                flag = False
                break
        if flag:
            return "".join(abbr)
    return ""

def getAbbreviation(word):
    if not word:
        return []
    if len(word) == 1:
        return [["1"], [word]]
    tmp = getAbbreviation(word[1:])
    res = []
    for t in tmp:
        res.append([word[0]] + t)
        if t[0].isdigit():
            t[0] = str(int(t[0]) + 1)
            res.append(t)
        else:
            res.append(["1"] + t)
    return res

def isValidAbbreviation(abbr, word):
    j = 0
    for i in xrange(len(abbr)):
        if abbr[i].isdigit():
            j += int(abbr[i])
        else:
            if j >= len(word):
                return False
            if abbr[i] != word[j]:
                return False
            j += 1
    return j == len(word)

print minAbbreviation("apple", ["plain", "amber", "blade"])
