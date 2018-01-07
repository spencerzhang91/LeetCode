// 461 Hamming Distance
object Solution {
    def hammingDistance(x: Int, y: Int): Int = {
        (x ^ y).toBinaryString.count(char => char == '1')
    }
}