"""
Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.
The returned array must be in sorted order.
Expected time complexity: O(n)
Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
Result: [3, 9, 15, 33]
nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
Result: [-23, -5, 1, 7]
"""

def sortTransformedArray(nums, a, b, c):
    if not nums:
        return []
    head, tail = 0, len(nums)-1
    res = []
    while head <= tail:
        h = nums[head] ** 2 * a + nums[head] * b + c
        t = nums[tail] ** 2 * a + nums[tail] * b + c
        if a <= 0:
            if h < t:
                res.append(h)
                head += 1
            else:
                res.append(t)
                tail -= 1
        else:
            if h > t:
                res.append(h)
                head += 1
            else:
                res.append(t)
                tail -= 1
    if a > 0:
        return res[::-1]
    return res
