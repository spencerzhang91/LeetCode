// 821. Shortest Distance to a Character
package main

import "fmt"
import "math"

func shortestToChar(S string, C byte) []int {
    prev := math.MinInt16
    dist := make([]int, 0)
    for i, c := range S {
        if byte(c) == C {
            prev = i
        }
        dist = append(dist, i-prev)
    }
    fmt.Println(dist)
    prev = math.MaxInt16
    for i := len(S)-1; i >= 0; i-- {
        if S[i] == C {
            prev = i
        }
        dist[i] = int(math.Min(float64(dist[i]), float64(prev-i)))
    }
    return dist
}


func main() {
    fmt.Println(shortestToChar("loveleetcode", 'e'))
}
