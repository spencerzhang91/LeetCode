// 198. House Robber
package main

func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) < 2 {
		return nums[0]
	}
	pprev := nums[0]
	prev := max(nums[0], nums[1])
	for i := 2; i < len(nums); i++ {
		curr := max(pprev+nums[i], prev)
		pprev = prev
		prev = curr
	}
	return max(pprev, prev)
}

func max(a int, b int) int {
	if a < b {
		return b
	}
	return a
}
