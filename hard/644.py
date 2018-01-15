"""
Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
"""

def findMaxAverage(nums, k):
    if k > len(nums):
        return 0
    min_avg = min(nums) * 1.0
    max_avg = max(nums) * 1.0
    while max_avg - min_avg > 1e-6:
        mid_avg = min_avg + (max_avg - min_avg) / 2
        if canReachAvg(nums, mid_avg, k):
            print mid_avg
            min_avg = mid_avg
        else:
            max_avg = mid_avg
    return min_avg

def canReachAvg(nums, avg, k):
    sums = [0] * (len(nums) + 1)
    prev = 0
    for i in xrange(1, len(nums)+1):
        sums[i] = sums[i-1] + nums[i-1] - avg
        if i >= k:
            if sums[i] >= prev:
                return True
            prev = min(prev, sums[i-k+1])
    return False


# print canReachAvg([1,12,-5,-6,50,3], 22, 4)


print findMaxAverage([1,12,-5,-6,50,3], 4)
