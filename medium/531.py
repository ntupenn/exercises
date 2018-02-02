"""
Given a picture consisting of black and white pixels, find the number of black lonely pixels.
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.
Example:
Input:
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.

Note:
The range of width and height of the input 2D array is [1,500].
"""

def findLonelyPixel(picture):
    if not picture or not picture[0]:
        return 0
    # rows = [0] * len(picture)
    # cols = [0] * len(picture[0])
    # cnt = 0
    # for i in xrange(len(picture)):
    #     for j in xrange(len(picture[0])):
    #         if picture[i][j] == "B":
    #             rows[i] += 1
    #             cols[j] += 1
    # for i in xrange(len(picture)):
    #     for j in xrange(len(picture[0])):
    #         if picture[i][j] == "B" and rows[i] == cols[j] == 1:
    #             cnt += 1
    # return cnt
    res = 0
    for i in xrange(len(picture)):
        cnt = 0
        idx = -1
        for j in xrange(len(picture[0])):
            if picture[i][j] == "B":
                cnt += 1
                idx = j
            if cnt > 1:
                break
        if cnt == 1:
            cnt = 0
            for ii in xrange(len(picture)):
                cnt += 1 if picture[ii][idx] == "B" else 0
                if cnt > 1:
                    break
            if cnt == 1:
                res += 1
    return res
