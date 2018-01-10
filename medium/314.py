"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
Examples:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,20,4,5,2,7],
    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
"""

import collections

def verticalOrder(root):
    if not root:
        return []
    check = collections.defaultdict(list)
    queue = collections.deque()
    queue.append((root, 0))
    l, r = 0, 0
    while queue:
        node, val = queue.popleft()
        if node.left:
            queue.append((node.left, val-1))
        if node.right:
            queue.append((node.right, val+1))
        check[val].append(node.val)
        l = min(l, val)
        r = max(r, val)
    res = []
    for i in xrange(l, r+1):
        res.append(check[i])
    return res

# Test

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.right = node8
node6.left = node9

print verticalOrder(node1)
