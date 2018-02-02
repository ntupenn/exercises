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
    if not root:
        return 0
    total, inc, dec = dfs(root)
    return total

def dfs(root):
    if not root.left and not root.right:
        return 1, 1, 1
    total = inc = dec = 1
    if root.left:
        lt, li, ld = dfs(root.left)
        if root.left.val + 1 == root.val:
            inc += li
        elif root.left.val - 1 == root.val:
            dec += ld
        total = max(total, lt)
    if root.right:
        rt, ri, rd = dfs(root.right)
        if root.right.val + 1 == root.val:
            inc = max(ri+1, inc)
        elif root.right.val - 1 == root.val:
            dec = max(rd+1, dec)
        total = max(total, rt)
    total = max(total, inc + dec - 1)
    return total, inc, dec
