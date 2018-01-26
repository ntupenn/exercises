"""
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:

Input:
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation:
    5
   /
  10

Sum: 15

   10
  /  \
 2    3

Sum: 15
Example 2:

Input:
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
Note:

The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000
"""

def checkEqualTree(root):
    if not root:
        return None
    check = collections.defaultdict(int)
    total = helper(root, check)
    if total == 0:
        return check[0] > 1
    return total % 2 == 0 and total / 2 in check

def helper(root, check):
    s = root.val
    if root.left:
        s += helper(root.left, check)
    if root.right:
        s += helper(root.right, check)
    check[s] += 1
    return s
