# 69 Sqrt(x)
# using binary search to build a sqrt function from scratch

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        head, tail = 0, x // 2 + 1
        while head <= tail:
            mid = (head + tail) // 2
            if mid * mid > x:
                tail = mid - 1
            elif mid * mid < x:
                head = mid + 1
            elif mid * mid == x:
                return mid
        return (head + tail) // 2

if __name__ == '__main__':
    test = Solution()
    print(test.mySqrt(9))
    
