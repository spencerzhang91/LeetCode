class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for item in nums:
            if item == 0:
                nums.remove(item)
                nums.append(item)

class Solution(object):
    def moveZeroes(self, nums):
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            else:
                i += 1
            j += 1
