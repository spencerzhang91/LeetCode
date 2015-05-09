class Solution:
    def countPrimes(self, n):
        if n <2: return 0
        i = 2
        boolist = [True] * n
        boolist[0] = False
        boolist[1] = False
        while i <= n ** 0.5:
            if boolist[i]:
                j = i
                while i *j < n:
                    boolist[i*j] = False
                    j += 1
            i += 1
        return sum(boolist)
