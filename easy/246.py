'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.
For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''

def isStrobogrammatic(num):
    if not num:
        return True
    start = 0
    end = len(num) - 1
    check = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    while start <= end:
        if num[start] not in check or check[num[start]] != num[end]:
            return False
        start += 1
        end -= 1
    return True
