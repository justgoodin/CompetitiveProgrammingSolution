#Link to the question below
#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        xRev: int

        if x<0:
            xRev = int("-"+str(x)[:0:-1])
        else:
            xRev = int(str(x)[::-1])

        return 0 if (-2**31>xRev or xRev>2**31-1) else xRev