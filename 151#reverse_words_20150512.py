class Solution:
    def reverseWords(sefl, s):
        wordlist = [char for char in s.split(' ') if char != '']        
        wordlist = wordlist[::-1]
        res = ''
        for i in range(len(wordlist)):            
            res += wordlist[i]
            res += ' '
        res = res[:-1]
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.reverseWords('hello'))
    print(test.reverseWords(''))
    print(test.reverseWords('   '))
    print(test.reverseWords('hello world and the heaven and hell'))
    print(test.reverseWords('   hello   world  '))
