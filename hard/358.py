"""
Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.
All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:
str = "aabbcc", k = 3
Result: "abcabc"
The same letters are at least distance 3 from each other.

Example 2:
str = "aaabc", k = 3
Answer: ""
It is not possible to rearrange the string.

Example 3:
str = "aaadbbcc", k = 2
Answer: "abacabcd"
Another possible answer is: "abcabcda"
The same letters are at least distance 2 from each other.
"""

import heapq

def rearrangeString(s, k):
    if not s:
        return s
    length = len(s)
    check = {}
    for c in s:
        check[c] = check.get(c, 0) + 1
    heap = []
    for c in check:
        heapq.heappush(heap, (-check[c], c))
    res = ""
    while heap:
        cnt = min(k, length)
        length -= cnt
        added = []
        for _ in xrange(cnt):
            if not heap:
                return ""
            size, c = heapq.heappop(heap)
            res += c
            size += 1
            if size != 0:
                added.append((size, c))
        for each in added:
            heapq.heappush(heap, each)
    return res
