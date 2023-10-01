class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reversed_ = str(x)[::-1]
        if original == reversed_:
            print( f" {x} is a palindrome")
            return True
        else :
            return False