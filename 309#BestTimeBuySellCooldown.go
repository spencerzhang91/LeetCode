// 309. Best Time to Buy and Sell Stock with Cooldown

package main
import "math"

func maxProfit(prices []int) int {
    ds := len(prices)
    if ds <= 1 {
        return 0
    }
    s0 := make([]int, ds) // not holding, can buy
    s1 := make([]int, ds) // holding, can sell, can rest
    s2 := make([]int, ds) // not holding, must rest
    s1[0] = -prices[0]
    s0[0] = 0
    s2[0] = math.MinInt16
    for i := 1; i < ds; i++ {
        s0[i] = max(s0[i - 1], s2[i - 1])
        s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
        s2[i] = s1[i - 1] + prices[i]
    }
    return max(s0[ds - 1], s2[ds - 1])
}

func max(a int, b int) int {
    if a < b {
        return b
    } else {
        return a
    }
}


func main() {
    prices := []int {1,2,3,0,2}

    fmt.Println(maxProfit(prices))
}