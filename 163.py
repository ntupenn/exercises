"""
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""

def findMissingRange(nums, lower, upper):
    if lower > upper:
        return []
    if not nums:
        return [str(lower) + "->" + str(upper)]
    if lower > nums[0] or upper < nums[-1]:
        return []
    start = lower
    res = []
    for num in nums:
        if num == start:
            start += 1
        elif num > start:
            if num - start == 1:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(num-1))
            start = num + 1
    if upper == start:
        res.append(str(start))
    elif upper > start:
        res.append(str(start) + "->" + str(upper))
    return res

print findMissingRange([0, 1, 3, 50, 75], 0, 99)
