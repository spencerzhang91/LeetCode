class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            nums = nums
        else:
            res = nums[-k%n:] + nums[:-k%n]
            for i in range(len(res)):
                nums[i] = res[i]
    
    # Dino's second solution below
    def rotate2(self, nums, k):
        n = len(nums) - k
        if n < 0:
           n = len(nums)+n
        print(n)
        nums = nums[n:] + nums[:n]


    
if __name__ == '__main__':
    test = Solution()
    nums = [1,2]
    k = -3
    print(test.rotate(nums, k))
    
