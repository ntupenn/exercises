"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
"""

def longestConsecutive(root):
    total, single = helper(root)
    return total

def helper(root):
    if not root:
        return 0, 0
    single = total = 1
    if root.left:
        left = helper(root.left)
        if abs(root.left.val - root.val) == 1:
            single += left[1]
            total += left[1]
        total = max(total, left[0])
    if root.right:
        right = helper(root.right)
        if abs(root.right.val - root.val) == 1:
            single = max(single, right[1] + 1)
            total += right[1]
        total = max(total, right[0])
    return total, single
