class Solution:
    # @return a string
    def countAndSay(self, n):
        string = '1'
        for x in range(n - 1):
        #while n > 1:
            count = 1
            temp = ""
            
            print('start outer', string)
            
            for i in range(len(string)-1):
                
                print('start inner', string)
                print(list(range(len(string)-1)))
                
                if string[i+1] != string[i]:
                    temp += str(count)
                    temp += string[i]
                    count = 1
                    
                    print('a', temp)
                    
                else:
                    count += 1
                    
                    print('b', temp, '|', count)
            print('end inner')        
            temp += str(count)
            temp += string[-1]
            
            print('c', temp)
            
            string = temp
            #n -= 1
        print('end')
        return string

if __name__ == '__main__':
    test = Solution()
    print(test.countAndSay(5))
