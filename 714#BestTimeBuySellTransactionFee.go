// 714. Best Time to Buy and Sell Stock with Transaction Fee
package main
import "fmt"

func maxProfit(prices []int, fee int) int {
    ds := len(prices)
    if ds <= 1 {
        return 0
    }
    s0 := make([]int, ds)    // Not holding, can buy, can rest
    s1 := make([]int, ds)    // Holding, not able to buy, can sell, can rest
    s0[0] = 0                // The max profit here is when no transaction is made
    s1[0] = -prices[0]       // State 1 initial profit
    for i := 1; i < ds; i++ {
        s0[i] = max(s0[i-1], s1[i-1]+prices[i]-fee) // max(rest, sell)
        s1[i] = max(s1[i-1], s0[i-1]-prices[i]) // max(rest, buy)
        // buy and sell one stock only pay once!
    }
    fmt.Println(s0)
    fmt.Println(s1)
    return max(s0[ds-1], s1[ds-1])
}

func max(a int, b int) int {
    if a < b {
        return b
    }
    return a
}

func main() {
    prices := []int {1, 3, 2, 8, 4, 9}
    fee := 2
    fmt.Println(maxProfit(prices, fee))
}

