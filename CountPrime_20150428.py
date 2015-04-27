class Solution:
    def countPrimes(self, n):
        n += 1
        boolist = [True for i in range(2,n)]
        i, m = 2, 0
        
        print(i,m)
        while i <= n ** 0.5:
            print('cc')
            if boolist[i]:
                print('bb')
            
                while i ** 2 + m * i < n:
                    print('aa')
                    j = i ** 2 + m * i
                    boolist[j] = False
                    m += 1
            i += 1
        return boolist


test = Solution()
print(test.countPrimes(10))
