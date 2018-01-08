"""
Problem:
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""

def wiggleSort(nums):
    if len(nums) < 2:
        return
    findKth(nums, 0, len(nums)-1, len(nums)/2)
    big = 1
    small = len(nums) - 1 if len(nums) % 2 == 1 else len(nums) - 2
    while big < small:
        nums[big], nums[small] = nums[small], nums[big]
        big += 2
        small -= 2

def findKth(nums, start, end, k):
    s, e = start, end
    tmp = nums[s]
    while s < e:
        while s < e and nums[e] >= tmp:
            e -= 1
        nums[s] = nums[e]
        while s < e and nums[s] < tmp:
            s += 1
        nums[e] = nums[s]
    nums[s] = tmp
    if s > k:
        findKth(nums, start, s-1, k)
    elif s < k:
        findKth(nums, s+1, end, k)
