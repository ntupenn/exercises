"""
Assume you have an array of length n initialized with all 0's and are given k update operations.
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.
Example:
Given:

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]
Output:
    [-2, 0, 3, 5, 3]
Explanation:
Initial state:
[ 0, 0, 0, 0, 0 ]
After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]
After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]
After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]
"""

def getModifiedArray(n, operations):
    # O(k)
    res = [0] * n
    for left, right, val in operations:
        res[left] += val
        if right + 1 < n:
            res[right+1] = -val
    prev = 0
    for i in xrange(n):
        res[i] += prev
        prev = res[i]
    return res

# def getModifiedArray(n, operations):
#     # O(klog(k))
#     res = [0] * n
#     updates = []
#     for s, e, d in operations:
#         updates.append((s, 0, d))
#         updates.append((e, 1, d))
#     updates.sort()
#     idx = 0
#     start = 0
#     for i in xrange(n):
#         if idx == len(updates):
#             break
#         end = 0
#         while idx < len(updates) and updates[idx][0] == i:
#             start += updates[idx][2] if updates[idx][1] == 0 else 0
#             end += updates[idx][2] if updates[idx][1] == 1 else 0
#             idx += 1
#         res[i] = start
#         start -= end
#     return res
