"""
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:

Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:

Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
"""

import collections

def wordsAbbreviation(words):
    if not words:
        return []
    abbrToWord = collections.defaultdict(list)
    wordToAbbr = {}
    for word in words:
        abbr = getShortestAbbr(word)
        abbrToWord[abbr].append(word)
        wordToAbbr[word] = abbr
    for abbr in abbrToWord:
        if len(abbrToWord[abbr]) == 1:
            continue
        for word in abbrToWord[abbr]:
            for size in xrange(2, len(word)-2):
                flag = True
                for next_word in abbrToWord[abbr]:
                    if next_word == word:
                        continue
                    if word[:size] == next_word[:size]:
                        flag = False
                        break
                if flag:
                    wordToAbbr[word] = word[:size] + str(len(word) - 1 - size) + word[-1]
                    break
            if wordToAbbr[word] == abbr:
                wordToAbbr[word] = word
    res = []
    for word in words:
        res.append(wordToAbbr[word])
    return res

def getShortestAbbr(word):
    if len(word) <= 3:
        return word
    return word[0] + str(len(word) - 2) + word[-1]
