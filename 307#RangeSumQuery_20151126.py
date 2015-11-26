# 305 Range Sum Query
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.updatedlist = []
        self.updateList()

    def updateList(self):
        if len(self.nums) >0:
            self.updatedlist.append(self.nums[0])
        for i in range(1,len(self.nums)):
            self.updatedlist.append(self.updatedlist[i-1] + self.nums[i])
        print(self.nums)
        print(self.updatedlist)



    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = self.updatedlist[j]
        if i >=1:
            sum -= self.updatedlist[i-1]
        return sum
        
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

if __name__ == "__main__":
    numArray = NumArray([1,2,3,4,5,6,7,8,9])
    res = numArray.sumRange(0, 1)
    print(res)