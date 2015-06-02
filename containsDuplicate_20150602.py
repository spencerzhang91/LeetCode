class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(nums) == 0:
            return False
        elif len(set(nums)) < len(nums):
            return True
        else:
            return False
