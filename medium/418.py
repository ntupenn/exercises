"""
Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.
Note:
A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word won't exceed 10.
1 <= rows, cols <= 20,000.
"""

def wordsTyping(sentence, rows, cols):
    s = " ".join(sentence)
    s += " "
    size = len(s)
    start = 0
    for i in xrange(rows):
        start += cols
        if s[start % size] == " ":
            start += 1
        else:
            while start > 0 and s[(start-1) % size] != " ":
                start -= 1
    return start / size

# def wordsTyping(sentence, rows, cols):
#     if rows == 0 or cols == 0:
#         return 0
#     i = j = 0
#     idx = 0
#     cnt = 0
#     while i < rows:
#         if len(sentence[idx]) + j - 1 <= cols - 1:
#             j += len(sentence[idx]) + 1
#             if j >= cols:
#                 j = 0
#                 i += 1
#             idx += 1
#             if idx == len(sentence):
#                 cnt += 1
#                 idx = 0
#         else:
#             i += 1
#             j = 0
#     return cnt
