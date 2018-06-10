class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """  
        dis = 0
        lmx = 0
        lc = 0
        rc = 0
        if seats[0] == 0:
            i = 0
            while seats[i] != 1:
                lc += 1
                i += 1
        if seats[-1] == 0:
            j = -1
            while seats[j] != 1:
                rc += 1
                j -= 1
            
        for i in seats:
            if i == 0:
                dis += 1
            else:
                if dis % 2 == 0:
                    lmx = max(lmx, dis // 2)
                else:
                    lmx = max(lmx, dis // 2 + 1)
                dis = 0
        return max(lc, rc, lmx)