#75 sort colors
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 1:
                nums.remove(i)
                nums.append(i)
        for i in nums:
            if i == 2:
                nums.remove(i)
                nums.append(i)
