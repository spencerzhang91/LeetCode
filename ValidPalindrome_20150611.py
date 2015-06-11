# using recursive way to solve but not efficient
class Solution:
    def isPalindrome(self, s):
        ss = [char.lower() for char in s if char.isalpha() or char.isdigit()]
        if len(ss) < 2:
            # base case
            return True
        else:
            # recursive case
            if ss[0] != ss[-1]:
                return False
            else:
                return self.isPalindrome(ss[1:-1])
            

if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome('are you kidding me'))
    print(test.isPalindrome('A man, a plan, a canal: Panama'))
    print(test.isPalindrome(''))
    print(test.isPalindrome('1a2'))
    print(test.isPalindrome('race e car'))
