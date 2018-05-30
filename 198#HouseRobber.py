# 198. House Robber

# Memoization solution: O(n) time, O(n) space
class Solution1:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        max_rob = [0] * len(nums)
        max_rob[0], max_rob[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_rob[i] = max(max_rob[i-2] + nums[i], max_rob[i-1])
        return max(max_rob[-1], max_rob[-2])

# Bottom up solution: O(n) time, O(1) space
class Solution2:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        pprev, prev = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(pprev + nums[i], prev)
            pprev = prev
            prev = curr
        return max(pprev, prev)
