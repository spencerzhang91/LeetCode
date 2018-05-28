# 746. Min Cost Climbing Stairs

# O(n) space solution:
class Solution1:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 3:
            return 0
        min_cost = [0] * len(cost)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        for i in range(2, len(cost)):
            min_cost[i] = min(min_cost[i-1], min_cost[i-2]) + cost[i]
        return min(min_cost[-1], min_cost[-2])

# O(1) space solution:
class Solution2(object):
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
