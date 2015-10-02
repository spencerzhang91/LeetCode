class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        n = len(nums)
        res = []
        return self.helper(nums, i, n, res)

    def helper(self, nums, i, n, res):
        if i == n:
            newperm = []
            for j in range(n):
                newperm.append(nums[j])
            res.append(newperm)
        else:
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                self.helper(nums, i+1, n, res)
                nums[i], nums[j] = nums[j], nums[i]
        return res

if __name__ == '__main__':
    test = Solution()
    L = [1,2,3,4]
    test.permute(L)
    
    
        
        
