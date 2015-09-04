class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        if l == 0:
            return 0
        if l == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1
        citations.sort()
        h = min(citations[0], l)
        for i in range(l - 1):
            fore_h = min(citations[i], l-i)
            next_h = min(citations[i+1], l-(i+1))
            if next_h >= fore_h:
                h = next_h
            else:
                break
        return h

if __name__ == '__main__':
    c = [0,1,0]
    test = Solution()
    h = test.hIndex(c)
    print(h)
            
