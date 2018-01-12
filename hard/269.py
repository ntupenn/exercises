"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, wherewords are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]


The correct order is: "wertf".

Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

import collections

def alienOrder(words):
    if not words:
        return []
    if len(words) == 1:
        return words[0]
    inbound = {}
    outbound = {}
    for word in words:
        for letter in word:
            inbound[letter] = 0
            outbound[letter] = set()
    for i in xrange(len(words)-1):
        w1, w2 = words[i], words[i+1]
        idx = 0
        while idx < len(w1) and idx < len(w2):
            if w1[idx] != w2[idx]:
                if w2[idx] not in outbound[w1[idx]]:
                    outbound[w1[idx]].add(w2[idx])
                    inbound[w2[idx]] += 1
                break
            idx += 1
    queue = collections.deque()
    for letter in inbound:
        if inbound[letter] == 0:
            queue.append(letter)
    res = []
    while queue:
        letter = queue.popleft()
        res.append(letter)
        for c in outbound[letter]:
            inbound[c] -= 1
            if inbound[c] == 0:
                queue.append(c)
    return "".join(res)
