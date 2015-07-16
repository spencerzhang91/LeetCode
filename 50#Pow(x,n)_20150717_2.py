class Solution:
    def myPow(self, x, n):
        if n < 0:
            x, n = 1/x, -n
        elif n == 0:
            return 1
        elif n == 1:
            return x
        mark_n = n
        mark_x = x
        
        while n > 0:
            x = x * x
            n = n // 2
            print('x = %d, n = %d' % (x, n))
        if mark_n % 2 == 0:
            return x
        else:
            return x / mark_x

if __name__ == '__main__':
    test = Solution()
    print(test.myPow(2, 10))
