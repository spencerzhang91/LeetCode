class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) != int(v2[i]):
                flag1, flag2 = int(v1[i]), int(v2[i])
                break
        else:
            if len(v1) == len(v2):
                return 0
            elif len(v1) > len(v2):
                if int(v1[-1]) == 0:
                    return 0
                return 1
            elif len(v1) < len(v2):
                if int(v2[-1]) == 0:
                    return 0
                return -1
        if flag1 > flag2:
            return 1
        else:
            return -1

if __name__ == '__main__':
    test = Solution()
    print(test.compareVersion('1','1.0000'))

    
