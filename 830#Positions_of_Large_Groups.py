class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) < 3:
            return []
        res = []
        i = 0
        while i < len(S) - 1:
            count = 1
            j = i + 1
            while j <= len(S) - 1 and S[j] == S[i]:
                j += 1
                count += 1
            if count >= 3:
                res.append([i, j-1])
            i = j
            count = 0
        return res