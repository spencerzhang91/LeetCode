# 121 Best Time to Buy and Sell Stock
# 121#maxProfit_20160413.py

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: list[int]
        :rtype: int
        """
        profit = 0
        currentMinPrice = prices[0] if len(prices) > 0
        