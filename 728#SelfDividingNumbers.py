class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = [i for i in range(left, right+1)]
        for num in range(left, right+1):
            digits = list(str(num))
            for digit in digits:
                if digit == "0" or num % int(digit) != 0:
                    res.remove(num)
                    break
        return res

class Solution2:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            digits = list(str(num))
            trace = 0
            for digit in digits:
                if digit != "0" and num % int(digit) == 0:
                    trace += 1
            if trace == len(digits):
                res.append(num)

        return res