class Solution:
    def majorityElement(self, nums):
        for element in set(nums):
            if nums.count(element) >= (len(nums)//2 + 1):
                return element
