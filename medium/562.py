"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""

def longestLine(matrix):
    if not matrix or not matrix[0]:
        return 0
    res = 0
    rows, cols = len(matrix), len(matrix[0])
    for i in xrange(rows):
        for j in xrange(cols):
            if matrix[i][j] == 0:
                continue
            if i == 0 or matrix[i-1][j] == 0:
                ii = i
                cnt = 0
                while ii < rows and matrix[ii][j] == 1:
                    ii += 1
                    cnt += 1
                if cnt > res:
                    res = cnt
            if j == 0 or matrix[i][j-1] == 0:
                jj = j
                cnt = 0
                while jj < cols and matrix[i][jj] == 1:
                    jj += 1
                    cnt += 1
                if cnt > res:
                    res = cnt
            if i == 0 or j == 0 or matrix[i-1][j-1] == 0:
                ii, jj = i, j
                cnt = 0
                while ii < rows and jj < cols and matrix[ii][jj] == 1:
                    cnt += 1
                    ii += 1
                    jj += 1
                if cnt > res:
                    res = cnt
            if i == 0 or j == cols-1 or matrix[i-1][j+1] == 0:
                ii, jj = i, j
                cnt = 0
                while ii < rows and jj >= 0 and matrix[ii][jj] == 1:
                    cnt += 1
                    ii += 1
                    jj -= 1
                if cnt > res:
                    res = cnt
    return res
