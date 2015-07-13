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
