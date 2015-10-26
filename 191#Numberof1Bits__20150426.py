'''
A function that takes an unsigned integer and returns the number of ’1' bits
it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
"00000000000000000000000000001011", so the function should return 3.
'''
class Solution:
    def hammingWeight(self, num):
        return bin(num).count('1')
        
if __name__ == '__main__':
    test = Solution()
    print(test.hammingWeight(11))
        
