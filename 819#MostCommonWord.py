# 819. Most Common Word
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = ''.join(map(str.lower, paragraph))
        for p in "!?',;.":
            paragraph = paragraph.replace(p, "")
        ls = paragraph.split(" ")
        words = set(ls)
        res = None
        count = 0
        for word in words:
            if word not in banned:
                temp = ls.count(word)
                if temp > count:
                    res = word
                    count = temp
        return res

if __name__ == "__main__":

    para = "Given a Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive. The answer is in lowercase."

    so = Solution()
    banned = ["of", "is", "are"]
    res = so.mostCommonWord(para, banned)
    print(res)