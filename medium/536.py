"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:

Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   /
  3   1 5
Note:

There will only be '(', ')', '-' and '0' ~ '9' in the input string.
"""

def str2tree(s):
    if not s:
        return None
    val = 0
    start = 0
    sign = 1
    if s[start] == "-":
        sign = -1
        start = 1
    elif s[start] == "+":
        start = 1
    while start < len(s) and s[start] != "(":
        val = val * 10 + int(s[start])
        start += 1
    root = TreeNode(sign * val)
    if start == len(s):
        return root
    end = start
    cnt = 0
    while end < len(s):
        if s[end] == "(":
            cnt += 1
        elif s[end] == ")":
            cnt -= 1
            if cnt == 0:
                break
        end += 1
    root.left = str2tree(s[start+1:end])
    start = end + 1
    if start == len(s):
        return root
    root.right = str2tree(s[start+1:-1])
    return root
