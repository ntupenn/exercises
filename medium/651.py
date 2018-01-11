"""
Imagine you have a special keyboard with the following keys:
Key 1: (A): Prints one 'A' on screen.
Key 2: (Ctrl-A): Select the whole screen.
Key 3: (Ctrl-C): Copy selection to buffer.
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation:
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A

Example 2:
Input: N = 7
Output: 9
Explanation:
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.
"""

import collections

def maxA(n):
    if n < 1:
        return 0
    # f[i][j]: max screen print with first i keys, buffer length j,
    f = collections.defaultdict(lambda:collections.defaultdict(int))
    f[0][0] = 0
    for i in xrange(n):
        for j in f[i]:
            # A
            f[i+1][j] = max(f[i+1][j], f[i][j] + 1)
            # ctrl-A, ctrl-C
            f[i+2][f[i][j]] = max(f[i+2][f[i][j]], f[i][j])
            # ctrl-V
            f[i+1][j] = max(f[i+1][j], f[i][j] + j)
    return max(f[n].values())
