# using python lists
class Solution:
    def isPalindrome(self, s):
        Purified = [char.lower() for char in s if char.isalpha() or char.isdigit()]
        Reversed = Purified[::-1]
        return Purified == Reversed


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

          
        
