class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        h = 0
        c = citations[0]
        num = len(citations)
        for i in range(1, num-1):
            if citations[i] > c:
                c = citations[i]
                num -= 1
                if num >= c:
                    h = c
            else:
                h = c
        return h

if __name__ == '__main__':
    c = [1,2,2,2]
    test = Solution()
    h = test.hIndex(c)
    print(h)
            
