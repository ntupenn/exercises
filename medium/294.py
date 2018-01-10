"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip twoconsecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""

def canWin(s):
    if len(s) < 2:
        return False
    check = {}
    return helper(s, check)

def helper(s, check):
    if s in check:
        return check[s]
    for i in xrange(len(s)-1):
        if s[i] == s[i+1] == "+":
            res = helper(s[:i] + "--" + s[i+2:], check)
            if not res:
                check[s] = True
                return True
    check[s] = False
    return False
