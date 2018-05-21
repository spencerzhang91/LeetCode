// 605. Can Place Flowers

package main

import "fmt"

func canPlaceFlowers(flowerbed []int, n int) bool {
    count := 0
    for i := 0; i < len(flowerbed) && count < n; i++ {
        if flowerbed[i] == 0 {
            var next int
            var prev int
            if i == len(flowerbed)-1 {
                next = 0
            } else {
                next = flowerbed[i+1]
            }
            if i == 0 {
                prev = 0
            } else {
                prev = flowerbed[i-1]
            }
            if next == 0 && prev == 0 {
                flowerbed[i] = 1
                count++
            }
        }
    }
    return count == n
}

func main() {
    fl := []int{1, 0, 0, 0, 1, 0, 1}
    fmt.Println(canPlaceFlowers(fl, 11))
}
