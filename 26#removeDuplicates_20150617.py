# original solution
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        m = len(nums) - 1
        while m > 0:
            if nums[m] == nums[m-1]:
                nums.pop(m)
            m -= 1
        return len(nums)


# almost the same but faster
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        m = len(nums) - 1
        while m > 0:
            if nums[m] == nums[m-1]:
                nums.remove(nums[m])
            m -= 1
        return len(nums)

if __name__ == '__main__':
    test = Solution()
    print(test.removeDuplicates([1,1,1,1,1,1]))
