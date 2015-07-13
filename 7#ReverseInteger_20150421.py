class Solution:
    def reverse(self, x):
        temp = list(str(x))
        temp.reverse()
        if int(x) != 0:
            while temp[0] == '0':
                temp.pop(0)
            if temp[-1] == '-':
                temp.pop()
                return int('-'+''.join(temp)) if int(''.join(temp)) <= 2**31 else 0
            return int(''.join(temp)) if int(''.join(temp)) <= 2**31 else 0
        return 0

        
