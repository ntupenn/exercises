"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
For example, given nums = [-2, 0, 1, 3], and target = 2.
Return 2. Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]
"""

def threeSumSmaller(nums, target):
    if len(nums) < 3:
        return 0
    nums.sort()
    cnt = 0
    for i in xrange(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < target:
                cnt += k - j
                j += 1
            else:
                k -= 1
    return cnt
