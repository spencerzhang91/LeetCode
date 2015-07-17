class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        sets = list(set(nums))
        return (sum(sets * 3) - sum(nums)) // 2
        


if __name__ == '__main__':
    L = [765, 765, 765, 96, 226, 96, 96, 579, 226, 226]
    test = Solution()
    print(test.singleNumber(L))
