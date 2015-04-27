# The easiest way to coue up with though also the slowest way to solve prime number problem.

class Solution:
    def countPrime(self, N):
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
print(test.countPrime(100000))
            
