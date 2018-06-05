// 646. Maximum Length of Pair Chain

package main
import "fmt"
import "sort"
import "math"

func findLongestChain(pairs [][]int) int {
    cur := math.MinInt32
    ans := 0
    sort.SliceStable(pairs, func(i, j int) bool {return pairs[i][1] < pairs[j][1]})
    for _, pair := range pairs {
        if cur < pair[0] {
            cur = pair[1]
            ans++
        }
    }
    return ans
}