# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        mid = (left + right) / 2
        while left <= right:
            if isBadVersion(mid):
                right = mid - 1
                mid = (left + right) / 2
            else:
                left = mid + 1
                mid = (left + right) / 2
        return right + 1
            
