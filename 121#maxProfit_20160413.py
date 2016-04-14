# 121 Best Time to Buy and Sell Stock
# 121#maxProfit_20160413.py

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: list[int]
        :rtype: int
        """
        profit = 0
        currentMinPrice = prices[0] if len(prices) > 0 else 0
        for i in range(1, len(prices)):
            currentMinPrice = min(currentMinPrice, prices[i])
            profit = max(profit, prices[i] - currentMinPrice)
            print("currentmin:", currentMinPrice, "profit:", profit)
        return profit

if __name__ == "__main__":

    test = Solution()
    prices = [1,2,3,4,5,10,20,40,3,2,1,20,24,100,2]
    profit = test.maxProfit(prices)
    print(profit)