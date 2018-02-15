// 344 Reverse String

object Solution {
    def reverseString(s: String): String = {
        val len: Int = s.size
        var k = len - 1
        val arr = new Array[Char](len)
        for (i <- 0 until len) {
            arr(k) = s(i)
            k -= 1
        }
        arr.mkString
    }
}