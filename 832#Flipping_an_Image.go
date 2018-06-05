package main

func flipAndInvertImage(A [][]int) [][]int {
	// row length:
	rl := len(A[0])
	for _, row := range A {
		for i := 0; i < (rl+1)/2; i++ {
			temp := row[i] ^ 1
			row[i] = row[rl-1-i] ^ 1
			row[rl-1-i] = temp
		}
	}
	return A
}
