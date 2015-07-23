# original solution
class Solution:
    def strStr(self, haystack, needle):
        len_n = len(needle)
        len_h = len(haystack)
        if len_n > len_h:
            return -1
        elif len_n == 0:
            return 0
        for i in range(len_h - len_n + 1):
            j = 0
            while haystack[i + j] == needle[j]:
                j += 1
                if len(needle) == j:
                    return i
        return -1


# more explicit approach
class Solution:
    def strStr(self, haystack, needle):
        len_n = len(needle)
        len_h = len(haystack)
        if len_n > len_h:
            return -1
        elif len_n == 0:
            return 0
        elif needle in haystack:
            return len(haystack.split(needle)[0])
        return -1
