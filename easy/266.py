'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
'''

def permutationIsPalindrome(s):
    if not s:
        return True
    check = set()
    for c in s:
        if c in check:
            check.remove(c)
        else:
            check.add(c)
    return len(check) < 2

print permutationIsPalindrome("code")
print permutationIsPalindrome("aab")
print permutationIsPalindrome("carerac")
