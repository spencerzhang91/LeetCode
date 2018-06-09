// 638. Shopping Offers
package main
import "fmt"

func shoppingOffers(price []int, special [][]int, needs []int) int {
    return shopping(price, special, needs)
}

func shopping(price []int, special [][]int, needs []int) int {
    res := dot(needs, price) // total price without using special offer
    for _, s := range special {
        clone := make([]int, len(needs))
        copy(clone, needs)
        var j int = 0
        for j = 0; j < len(needs); j++ {
            diff := clone[j] - s[j]
            if diff < 0 {
                break
            }
            clone[j] = diff
        }
        if j == len(needs) {
            res = min(res, s[j] + shopping(price, special, clone))
        }
    }
    return res
}

func dot(a []int, b []int) int {
    sum := 0
    for i := 0; i < len(a); i++ {
        sum += a[i] * b[i]
    }
    return sum
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}

func main() {
    price := []int {2, 5}
    special := [][]int {{3, 0, 5}, {1, 2, 10}}
    needs := []int {3, 2}

    res := shoppingOffers(price, special, needs)
    fmt.Println(res)
}