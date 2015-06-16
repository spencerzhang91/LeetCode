class Solution:
    # @return a string
    def countAndSay(self, n):
        string = str(1)
        while n > 1:
            count = 1
            temp = ""
            for i in range(1, len(string)):
                if string[i] != string[i-1]:
                    temp += str(count)
                    temp += string[i-1]
                    count = 1
                else:
                    count += 1
            temp += str(count)
            temp += string[-1]
            string = temp
            n -= 1
        return string

if __name__ == '__main__':
    test = Solution()
    print(test.countAndSay(10))
