from itertools import combinations as cb
from time import time
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) <= 3:
            return sum(nums)
        sums = []
        for coup in cb(nums, 3):
            if sum(coup) not in sums:
                sums.append(sum(coup))
        v = [abs(item - target) for item in sums]
        return target + min(v) if target + min(v) in sums else target - min(v)

if __name__ == '__main__':
    test = Solution()
    t1 = time()
    res = test.threeSumClosest([1,1,1,1,1,1,1],
                               11)
    t2 = time()
    print(res)
    print(t2 - t1)

# This method can not pass leetcode OJ because exceeded time limits.
# A more efficient approach is needed.
