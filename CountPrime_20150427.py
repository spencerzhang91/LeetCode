from time import time

class Solution:
    def countPrimes(self, N):
        count = 1
        for num in range(2,N):
            if self.isPrime(num):
                count += 1
        return count

    def isPrime(self, num):
        par = num // 2
        res = None
        while par > 1:
            if num % par == 0:
                res = False
                break
            par -= 1
        else:
            return True

test = Solution()
t1 = time()
print(test.countPrimes(15000))
t2 = time()
print(t2 - t1)
