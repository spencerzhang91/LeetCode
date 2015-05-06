class Solution:
    def longestCommonPrefix(self, strs):
        n = 0
        if len(strs) == 0:
            return ""
        elif len(strs)==1:
            return strs[0]
        else:
            for i in range(len(strs[0])):
                for j in range(1,len(strs)):
                    if i > len(strs[j])-1:
                        return strs[0][0:n]
                    if strs[j][i]!=strs[0][i]:
                        return strs[0][0:n]            
                n += 1
            return strs[0]

if __name__ == '__main__':
    test = Solution()    
    print(test.longestCommonPrefix(['aabcd', 'aabd', 'aa']))
