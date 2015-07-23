#228
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        if len(nums) == 0:
            res = []
        elif len(nums) == 1:
            res.append(str(nums[0]))
        else:
            start = nums[0]
            stop = nums[0]
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] > 1:
                    stop = nums[i-1]
                    if start < stop:
                        res.append("%d->%d" % (start, stop))
                    else:
                        res.append("%d" % stop)
                    start = nums[i]
                else:
                    stop = nums[i]
            if start < stop:
                res.append("%d->%d" % (start, stop))
            else:
                res.append("%d" % start)
        return res
        


# approach recursive
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        def getRange(begin, end):
            return str(begin)+"->" + str(end) if begin != end else str(begin)
        n = len(nums)
        if n==0:
            return []
        res = []
        pre = start = nums[0]
        for num in nums:
            cur = num 
            if cur - pre > 1:
                res.append(getRange(start, pre))
                start = cur
            if cur == nums[-1]:
                res.append(getRange(start, cur))
            pre = cur
        return res        

        
