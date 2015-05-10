class Solution:
    def twoSum(self, nums, target):
        can = [num for num in nums if num <= target]
        for item in can:
            temp = target - item
            nums[nums.index(item)] = 'x'
            if temp in can:
                return nums.index('x')+1, nums.index(temp)+1
            else:
                nums[nums.index('x')] = item

            

if __name__ == "__main__":
    test = Solution()
    a = test.twoSum([1,2,3,11,22,33], 44)
    print(a)
