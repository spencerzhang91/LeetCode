class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0:
            res = []
        elif numRows == 1:
            res = [[1]]
        else:
            res = [[1],[1,1]]
            while numRows > 2:
                cur = []
                last = res[-1]
                cur.append(1)
                for i in range(len(last)-1):
                    cur.append(last[i] + last[i+1])                
                cur.append(1)
                res.append(cur)
                numRows -= 1            
        return res[numRows+1]

if __name__ == '__main__':
    test = Solution()
    print(test.generate(5))
    
