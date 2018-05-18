class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(map(lambda x: 1 - x, row[::-1])) for row in A]