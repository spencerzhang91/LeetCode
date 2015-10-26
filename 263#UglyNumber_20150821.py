# 263 ugly number
# first solution trying to use a shieve, but memory error
class Solution:
    def isUgly(self, num):
        if num < 2:
            return True
        boolist = [False] * (num + 1)
        boolist[0] = False
        boolist[1] = True
        for facts in [2, 3, 5, 6, 10, 15]:
            boolist = self.setval(facts, num, boolist)
        print(boolist[num])
        
    def setval(self, fact, top, array):
        i = 1
        if fact in [2, 3, 5]:
            while fact ** i < top + 1:
                array[fact ** i] = True
                i += 1
        elif fact in [6, 10, 15]:
            while fact * i < top + 1:
                array[fact * i] = True
                i += 1
        else:
            print("Wrong factor!")
        return array

# second solution: much simpler and efficient
class Solution2:
    def isUgly(self, num):
        if num == 0:
            return False
        if num == 1:
            return True
        for p in [2, 3, 5]:
            while num % p == 0:
                num /= p
        return num == 1

if __name__ == "__main__":
    test = Solution()
    test.isUgly(10230913) # false
            
