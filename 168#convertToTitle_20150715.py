# 168 recursive approach 1
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        if n < 27:
            return chr(64 + n)
        return self.convertToTitle((n-((n-1)%26+1))//26) + self.convertToTitle((n-1)%26+1)

    
if __name__ == '__main__':
    test = Solution()
    for i in range(1, 96):
        print(i,'->',test.convertToTitle(i))

        
