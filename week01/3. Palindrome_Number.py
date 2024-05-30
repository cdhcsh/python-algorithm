import sys
def isPalindrome(x):
    if str(x) != str(x)[::-1]:
        return False
    else:
        return True