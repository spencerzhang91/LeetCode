// 746. Min Cost Climbing Stairs
package main

import "fmt"
// O(1) space solution
func minCostClimbingStairs1(cost []int) int {
    f1 := 0
    f2 := 0
    for i := len(cost)-1; i >= 0; i-- {
        f0 := cost[i] + min(f1, f2)
        f2 = f1
        f1 = f0
    }
    return min(f1, f2)
}

// Dynamic Programming
func minCostClimbingStairs2(cost []int) int {
    min_cost := make([]int, len(cost))
    min_cost[0] = cost[0]
    min_cost[1] = cost[1]
    for i := 2; i <= s-1; i++ {
        min_cost[i] = min(min_cost[i-1], min_cost[i-2]) + cost[i]
    }
    return min(min_cost[s-1], min_cost[s-2])
}

func min(a int, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}


func main() {
    cost := []int {1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
    sum := minCostClimbingStairs2(cost)
    fmt.Println(sum)
}