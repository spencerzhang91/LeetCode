// 343. Integer Break
package main
import "math"

func integerBreak(n int) int {
    if n == 2 {
        return 1
    } else if n == 3 {
        return 2
    } else if n % 3 == 0 {
        return int(math.Pow(float64(3), float64(n/3)))
    } else if n % 3 == 1 {
        return 2 * 2 * int(math.Pow(float64(3), float64((n-4)/3)))
    }
    return 2 * int(math.Pow(float64(3), float64(n/3)))
}
