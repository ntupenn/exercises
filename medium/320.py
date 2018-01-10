"""
Write a function to generate the generalized abbreviations of a word.
Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""

def findAllAbbreviations(word):
    if not word:
        return [""]
    if len(word) == 1:
        return [word, "1"]
    tmp = findAllAbbreviations(word[1:])
    res = []
    for t in tmp:
        res.append(word[0] + t)
        count = 0
        idx = 0
        while idx < len(t) and t[idx].isdigit():
            count = count * 10 + int(t[idx])
            idx += 1
        count += 1
        res.append(str(count) + t[idx:])
    return res
