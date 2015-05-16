class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            i = 0
            while x // 10 ** i > 0:
                i += 1
            while i > 0:
                head = x // 10 ** (i-1)
                tail = x % 10
                x = int((x - x//10**(i-1)*10**(i-1) - x%10)/10)
                i -= 2
                if head != tail:
                    return False
            return True

if __name__ == '__main__':    
    test = Solution()

    print(test.isPalindrome(1254321))
    print('-'*10)

    print(test.isPalindrome(1))
    print('-'*10)

    print(test.isPalindrome(11))
    print('-'*10)

    print(test.isPalindrome(12121))
    print('-'*10)

    print(test.isPalindrome(0))
    print('-'*10)

    print(test.isPalindrome(-3))
