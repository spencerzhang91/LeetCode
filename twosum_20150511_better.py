class Solution:
    def twoSum(self, num, target):
        map_n = {}
        for i in range(len(num)):
            if num[i] not in map_n:
                map_n[target - num[i]] = i
                print(i, ':', num[i])
                print(map_n)
            else:
                return map_n[num[i]] + 1, i + 1
        return -1, -1

if __name__ == "__main__":
    
    test = Solution()
    a = test.twoSum([1,43], 44)
    print(a)
