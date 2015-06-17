class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        for i in range(1,n):
            while i < n and nums[i-1] == nums[i]:
                nums.remove(nums[i-1])
                n -= 1
        return n


if __name__ == '__main__':
    test = Solution()
    print(test.removeDuplicates([1,1,1,1,1,1]))
