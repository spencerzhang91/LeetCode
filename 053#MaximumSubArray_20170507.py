class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        max_array = [0] * length
        max_array[length-1] = nums[length-1]
        curr_max = max_array[length-1]
        for j in range(2, length+1):
            if max_array[length-j+1] >= 0:
                max_array[length-j] = nums[length-j] + max_array[length-j+1]
            else:
                max_array[length-j] = nums[length-j]
            if max_array[length-j] > curr_max:
                curr_max = max_array[length-j]
        return curr_max

s = Solution()
maxsum = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(maxsum)