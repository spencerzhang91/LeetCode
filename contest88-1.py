class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        new_shift = [0] * len(shifts)
        new_shift[0] = sum(shifts)
        for i in range(1, len(shifts)):
            new_shift[i] = new_shift[i - 1] - shifts[i - 1]
        return "".join(list(map(lambda pair: chr(list(map(lambda x: (x - 122 + 96) if x > 122 else x, [ord(pair[1])+pair[0]]))[0]), zip(map(lambda x: x % 26, new_shift), list(S)))))
