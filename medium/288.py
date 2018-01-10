"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
a) it                      --> it    (no abbreviation)
     1
b) d|o|g                   --> d1g
              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n
              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
Example:
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""

import collections

class ValidWordAbbreviation:
    def __init__(self, dictionary):
        self.check = collections.defaultdict(list)
        for w in dictionary:
            key = self.findAbbreviation(w)
            self.check[key].append(w)

    def isUnique(self, word):
        key = self.findAbbreviation(word)
        if key in self.check:
            return len(self.check[key]) == 1 and self.check[key][0] == word
        return True

    def findAbbreviation(self, word):
        if len(word) < 3:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
