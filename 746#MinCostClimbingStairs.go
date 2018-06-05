// 746. Min Cost Climbing Stairs
package main

// O(1) space solution
func minCostClimbingStairs1(cost []int) int {
	f1 := 0
	f2 := 0
	for i := len(cost) - 1; i >= 0; i-- {
		f0 := cost[i] + min(f1, f2)
		f2 = f1
		f1 = f0
	}
	return min(f1, f2)
}

// Dynamic Programming
func minCostClimbingStairs2(cost []int) int {
	s := len(cost)
	minCost := make([]int, len(cost))
	minCost[0] = cost[0]
	minCost[1] = cost[1]
	for i := 2; i <= s-1; i++ {
		minCost[i] = min(minCost[i-1], minCost[i-2]) + cost[i]
	}
	return min(minCost[s-1], minCost[s-2])
}
