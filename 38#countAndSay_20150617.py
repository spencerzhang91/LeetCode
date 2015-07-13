class Solution:
    def countAndSay(self, n):
        string = '1'
        for x in range(n - 1):
            count = 1
            temp = ""
            for i in range(len(string)-1):
                if string[i+1] != string[i]:
                    temp += str(count)
                    temp += string[i]
                    count = 1    
                else:
                    count += 1     
            temp += str(count)
            temp += string[-1]
            string = temp
        return string

if __name__ == '__main__':
    test = Solution()
    print(test.countAndSay(5))
