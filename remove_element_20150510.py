class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        return len(nums) - nums.count(val)



class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        n = 0
        for i in range(0,len(A)):
            if A[i]==elem:
                n+=1
        
        for i in range(0,n):
            A.remove(elem)
        return len(A)


