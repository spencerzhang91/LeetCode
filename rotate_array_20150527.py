class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            nums = nums
        else:
            res = nums[-k%n:] + nums[:-k%n]
            for i in range(len(res)):
                nums[i] = res[i]
                
        # return nums


    
if __name__ == '__main__':
    test = Solution()
    nums = [1,2]
    k = 1
    print(test.rotate(nums, k))
    
