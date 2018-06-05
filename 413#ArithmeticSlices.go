// 413 Arithmetic Slices
package main

func numberOfArithmeticSlices(A []int) int {
	count := 0
	if len(A) < 3 {
		return count
	}
	leng := 0
	for curr := 1; curr < len(A)-1; curr++ {
		if A[curr+1]-A[curr] == A[curr]-A[curr-1] {
			leng++
			count += leng
		} else {
			leng = 0
		}
	}
	return count
}
