"""
Given a binary tree where every node has a unique value, and a target key k, find the closest leaf node to target k in the tree.
A node is called a leaf if it has no children.
In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:
Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2
Output: 2 (or 3)
Explanation: Either 2 or 3 is the closest leaf node to 1.

Example 2:
Input:
root = [1], k = 1
Output: 1
Explanation: The closest leaf node is the root node itself.

Example 3:
Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6
Output: 3

Explanation: The leaf node with value 3 (and not the leaf node with value 6) is closest to the node with value 2.

Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
"""

def findClosestLeaf(root, k):
    dummy = TreeNode(k+1)
    dummy.left = root
    node, parent = findNode(root, dummy, k)
    if not node:
        return -1
    d1, n1 = shortest(node)
    d2, n2 = shortest(parent)
    return n1 if d1 < d2 + 1 else n2

def findNode(root, parent, k):
    if not root:
        return None, parent
    if root.val == k:
        return root, parent
    left = findNode(root.left, root, k)
    if left[0]:
        return left
    right = findNode(root.right, root, k)
    if right[0]:
        return right
    return None, parent

def shortest(node):
    if not node.left and not node.right:
        return 1, node
    d = float('inf')
    n = None
    if node.left:
        left = shortest(node.left)
        d = left[0]
        n = left[1]
    if node.right:
        right = shortest(node.right)
        if right[0] < d:
            d = right[0]
            n = right[1]
    return d + 1, n
