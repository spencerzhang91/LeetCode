# 258 Add Digits

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if num == 0:
            return 0
        return 1 + ((num - 1) % 9)

if __name__ == '__main__':
    test = Solution()
    print(test.addDigits(0))
