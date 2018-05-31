// 647. Palindromic Substrings
package main

func countSubstrings(s string) int {
    N := len(s)
    res := 0
    for center := 0; center < 2*N; center++ {
        left := center / 2
        right := left + center % 2
        for left >= 0 && right < N && s[left] == s[right] {
            res++
            left--
            right++
        }
    }
    return res
}