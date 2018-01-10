"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given set of points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?

Hint:

Find the smallest and largest x-value for all points.
If there is a line then it should be at y = (minX + maxX) / 2.
For each point, make sure that it has a reflected point in the opposite side.
"""

def isReflected(points):
    if not points:
        return True
    check = set()
    l = r = points[0][0]
    for x, y in points:
        x *= 1.0
        check.add((x, y))
        l = min(l, x)
        r = max(r, x)
    m = l + (r - l) / 2.0
    for x, y in points:
        xx = m + m - x
        if (xx, y) not in check:
            return False
    return True
