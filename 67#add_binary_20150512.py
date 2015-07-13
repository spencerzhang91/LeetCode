class Solution:
    def addBinary(self, a, b):
        def bin_to_int(bstring):
            res = 0
            for i in range(len(bstring)):
                res += int(bstring[i]) * (2 ** (len(bstring) - i-1))
            return res
        return str(bin(bin_to_int(a) + bin_to_int(b)))[2:]
                
if __name__ == '__main__':
    test = Solution()
    print(test.addBinary('1', '11'))
    

