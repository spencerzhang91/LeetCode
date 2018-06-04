// 712. Minimum ASCII Delete Sum for Two Strings
package main
import "fmt"

func minimumDeleteSum(s1 string, s2 string) int {
    ls1 := len(s1)
    ls2 := len(s2)
    sum := init2dSlice(ls1+1, ls2+1)
    sum[0][0] = 0
    // s1 set as row, s2 set as column
    for i := 1; i <= ls1; i++ {
        sum[i][0] = sum[i-1][0] + int(s1[i-1])
    }
    for j := 1; j <= ls2; j++ {
        sum[0][j] = sum[0][j-1] + int(s2[j-1])
    }
    for i := 1; i <= ls1; i++ {
        for j := 1; j <= ls2; j++ {
            if s1[i-1] == s2[j-1] {
                sum[i][j] = sum[i-1][j-1]
            } else {
                sum[i][j] = min(sum[i][j-1] + int(s2[j-1]),
                                sum[i-1][j] + int(s1[i-1]))
            }
        }
    }
    fmt.Println(sum)
    return sum[ls1][ls2]
}

func init2dSlice(dx int, dy int) [][]int {
    sum := make([][]int, dx)
    for i := 0; i < dx; i++ {
        sum[i] = make([]int, dy)
    }
    return sum
}

func min(a int, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}

func main() {
    s1 := "sea"
    s2 := "eaten"
    res := minimumDeleteSum(s1, s2)
    fmt.Println(res)
}