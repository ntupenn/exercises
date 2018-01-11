'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''

def findClosest(root, target):
    if not root:
        return None
    res = root.val
    while root:
        if root.val == target:
            return target
        if abs(root.val - target) < abs(res - target):
            res = root.val
        if root.val > target:
            root = root.left
        else:
            root = root.right
    return res
