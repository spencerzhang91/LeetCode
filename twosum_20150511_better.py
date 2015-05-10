class Solution:
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i
            else:
                return map[num[i]] + 1, i + 1
        return -1, -1

if __name__ == "__main__":
    
    test = Solution()
    a = test.twoSum([1,2,3,11,22,33], 44)
    print(a)
