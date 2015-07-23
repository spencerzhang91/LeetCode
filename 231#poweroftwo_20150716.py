# 231 iterative approach
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        while n >= 2:
            if n % 2 != 0:
                return False
            else:
                n /= 2
        return True

# 231 using bitwise expression
class Solution:
    def isPowerOfTwo(self, n):
        return n&(n-1) == 0 and n > 0
