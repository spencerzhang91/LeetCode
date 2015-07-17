class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = nums[0]
        for item in nums[1:]:
            res ^= item
        return res

if __name__ == '__main__':
    L = [765, 765, 96, 96, 579, 226, 226]
    test = Solution()
    print(test.singleNumber(L))
