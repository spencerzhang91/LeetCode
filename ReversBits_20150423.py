class Solution:
    def reverseBits(self, num):
        bit = bin(num)[:2] + '0' * (34 - len(bin(num))) + bin(num)[2:]
        bit_reversed = '0b'+ bit[2:][::-1]
        return int(bit_reversed,2)

# self test code below
if __name__ == '__main__':
    instance = Solution()
    test = instance.reverseBits(100)
    print(test)
