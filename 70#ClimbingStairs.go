// 70. Climbing Stairs
package main
import "fmt"

// fibonacci number method
func climbStairs1(n int) int {
    if n == 1 {
        return 1
    }
    first := 1
    second := 2
    for i := 3; i < n+1; i++ {
        third := first + second
        first = second
        second = third
    }
    return second
}

// dynamic programming solution
func climbStairs2(n int) int {
    if n == 1 {
        return 1
    }
    dp := make([]int, n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i := 3; i < n+1; i++ {
        dp[i] = dp[i-1] + dp[i-2]
    }
    return dp[n]
}

func main() {
    res1 := climbStairs1(10)
    res2 := climbStairs2(10)
    fmt.Println(res1, res2)
}