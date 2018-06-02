// 338. Counting Bit
package main
import "fmt"
import "strconv"

func countBits(num int) []int {
    f := make([]int, num+1)
    for i := 1; i <= num; i++ {
        f[i] = f[i >> 1] + (i & 1)
    }
    return f
}

func main() {
    fmt.Println(countBits(5))

    for i := int64(0); i < 16; i++ {
        fmt.Println(strconv.FormatInt(i, 2))
    }
    
}