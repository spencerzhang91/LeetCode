# 70. Climbing Stairs
# fibonacci number solution
class Solution1:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second

# dynamic programming solution
class Solution2:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [1, 1, 2]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]