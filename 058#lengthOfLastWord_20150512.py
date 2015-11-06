class Solution:
    def lengthOfLastWord(sefl, s):
        wordlist = [char for char in s.split(' ') if char != '']
        if len(wordlist) < 1:
            return 0
        return len(wordlist[-1])

if __name__ == '__main__':
    test = Solution()
    print(test.lengthOfLastWord('hello'))
    print(test.lengthOfLastWord(''))
    print(test.lengthOfLastWord('   '))
    print(test.lengthOfLastWord('hello world'))
    print(test.lengthOfLastWord('hello   world  '))
