// 121 Best Time to Buy and Sell Stock
// 121#maxProfit_20160414.js

var maxProfit = funtion(prices) {
    var profit = 0;
    var currentMinPrice = (prices.length > 0)? prices[0]: 0;
    for (var i = 1; i < prices.length; i++) {
        currentMinPrice = Math.min(currentMinPrice, prices[i]);
        profit = Math.max(profit, prices[i] - currentMinPrice);
    }
    return profit;
};

var prices = [1,2,3,4,5,10,20,40,3,2,1,20,24,100,2];
var profit = maxProfit(prices);

println(profit);