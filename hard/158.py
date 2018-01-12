"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""


leftover = []
def read(buff, n):
    global leftover
    if len(leftover) >= n:
        buff += leftover[:n]
        leftover = leftover[n:]
        return n
    buff += leftover
    cnt += len(leftover)
    n -= len(leftover)
    leftover = []
    while n > 0:
        tmp = []
        tmp_n = read4(tmp)
        if tmp_n == 0:
            return cnt
        if n >= tmp_n:
            cnt += tmp_n
            n -= tmp_n
            buff += tmp[:n]
        else:
            cnt += n
            n = 0
            buff += tmp[:n]
            leftover = tmp[n:]
    return cnt
