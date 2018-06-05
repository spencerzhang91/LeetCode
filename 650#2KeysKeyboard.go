// 650. 2 Keys Keyboard
package main

func minSteps(n int) int {
	ans := 0
	d := 2
	for n > 1 {
		for n%d == 0 {
			ans += d
			n /= d
		}
		d++
	}
	return ans
}

/*
Hi, I'd like to share my math understanding of this problem.
This problem is actually a Prime factorization problem.
let's say the target number is 12.

you have two ways to get 12 with minimum steps.
12 = 6+6; 6=3+3; 3= 1+1+1. total steps is 7. OR
12= 4+4+4; 4=2+2; 2=1+1. total steps is also 7.
which means, whatever you decide to paste, as long as you paste a prime number times, the result will be optimum and this prime number is in its prime factorization.

Here is the prove:

A = a_1a_2...a_n. where a1 to an are all prime number(may have duplicates).
let A_m = a_1*...a_m.
B_m is the total steps to get A_m.
B_(m+1)=B_m+a_(m+1). copy all than paste (a_(m+1)-1) times, total a_(m+1) times.
so, as you can see, from B_m to B_m+1 is just add some constant number, there is NO addition between different .
B = a_1+a_2...+a_n.
the result is a constant number correspond to A itself. So, the sequence of how you use this prime number will not affect the result.
still use 12 as example: 12 = 22*3. 7=2+2+3.

As for the part why this is optimum
if you just do a factorization:
A=a_1a_2...c_1...a_n, where c_1=a_ka_(k+1)...*a_(k+l),
c1>=a_k+a_(k+1)+...+a_(k+l)
Source: https://leetcode.com/problems/2-keys-keyboard/discuss/105909/Math-Facts
*/
