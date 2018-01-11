"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""

def boldWords(s, dictionary):
    if not s or not dictionary:
        return s
    check = []
    d = set(dictionary)
    for i in xrange(len(s)):
        for l in xrange(1, len(s) - i + 1):
            if s[i:i+l] in d:
                check.append((i, 0))
                check.append((i+l, 1))
    check.sort()
    cnt = 0
    bold = []
    for idx, info in check:
        if info == 0:
            if cnt == 0:
                bold.append(idx)
            cnt += 1
        else:
            cnt -= 1
            if cnt == 0:
                bold.append(idx)
    res = ""
    end = 0
    for start_idx in xrange(0, len(bold), 2):
        res += s[end:bold[start_idx]]
        end = bold[start_idx+1]
        res += "<b>" + s[bold[start_idx]:end] + "</b>"
    res += s[end:]
    return res
