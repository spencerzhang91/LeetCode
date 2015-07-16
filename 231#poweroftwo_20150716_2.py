# 231 using bitwise expression
class Solution:
    def isPowerOfTwo(self, n):
        return n&(n-1) == 0 and n > 0
        
