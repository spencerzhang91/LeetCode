#275 H-index ii
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) / 2
            if N - mid > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return N - left



