"""
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""

def longestConsecutive(root):
    if not root:
        return 0
    total, curr = helper(root)
    return total

def helper(root):
    total = curr = 1
    if root.left:
        left = helper(root.left)
        if root.left.val == root.val + 1:
            curr = left[1] + 1
        total = max(curr, left[0])
    if root.right:
        right = helper(root.right)
        if root.right.val == root.val + 1:
            curr = max(curr, right[1] + 1)
        total = max(curr, right[0])
    return total, curr
