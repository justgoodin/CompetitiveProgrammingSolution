#Link to the question below
#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        
        return True if xStr == xStr[::-1] else False