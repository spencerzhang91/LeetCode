// 830. Positions of Large Groups

package main

import "fmt"

func largeGroupPositions(S string) [][]int {
	if len(S) < 3 {
		return make([][]int, 0)
	}
	res := [][]int{}
	i := 0
	for i < len(S)-1 {
		count := 1
		j := i + 1
		for (j <= len(S)-1) && (S[j] == S[i]) {
			j += 1
			count += 1
		}
		if count >= 3 {
			pair := []int{i, j - 1}
			res = append(res, pair)
		}
		i = j
	}
	return res
}

func main() {
	str := "abbxxxxzzy"
	res := largeGroupPositions(str)
	fmt.Println(str)
	fmt.Println(res)
}
