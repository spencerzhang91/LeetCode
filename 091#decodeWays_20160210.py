# 91 Decode Ways
class Solution(object):   
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0: return 0
        ways = [0] * (len(s) + 1)
        if s[0] == '0':
            ways[0] = 0
        else:
            ways[0] = ways[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != '0':
                ways[i] += ways[i-1]
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                ways[i] += ways[i-2]
        return ways[len(s)]

if __name__ == "__main__":
    string1 = "131111341111275111"
    string2 = "121212"
    test = Solution()
    ways = test.numDecodings(string1)
    print(ways)