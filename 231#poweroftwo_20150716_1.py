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
