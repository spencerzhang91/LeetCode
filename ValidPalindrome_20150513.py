class Solution:
    def isPalindrome(self, s):
        Purified = [char.lower() for char in s if char.isalpha() or char.isdigit()]
        Reversed = Purified[::-1]
        return Purified == Reversed

if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome('are you kidding me'))
    print(test.isPalindrome('A man, a plan, a canal: Panama'))
    print(test.isPalindrome(''))
    print(test.isPalindrome('1a2'))
    print(test.isPalindrome('race e car'))
          
        
