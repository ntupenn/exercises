"""
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.
"""

def isConvex(points):
    size = len(points)
    if size < 3:
        return False
    prev = 0
    for i in xrange(size):
        p0, p1, p2 = points[i], points[(i+1) % size], points[(i+2) % size]
        curr = crossProduct(p0, p1, p2)
        if curr * prev < 0:
            return False
        prev = curr
    return True

def crossProduct(p0, p1, p2):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
