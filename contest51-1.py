class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        operators = ["+", "D", "C"]
        cal_list = []
        if len(ops) <= 1 and ops[0] not in operators:
            #print(ops)
            return ops[0]
        if len(ops) <= 1 and ops[0] in operators:
            #print(ops)
            return 0
        for s in ops:
            if s not in operators:
                cal_list.append(int(s))               
            else:
                if s == "+":
                    cal_list.append(int(cal_list[-1]) + int(cal_list[-2]))
                elif s == "D":
                    cal_list.append(int(cal_list[-1]) * 2)
                elif s == "C":
                    cal_list.pop()
            #print(cal_list)
        return sum(cal_list)

if __name__ == '__main__':

    ls1 = ["5","2","C","D","+"]
    ls2 = ["5","-2","4","C","D","9","+","+"]
    ls3 = ['1','2','3','C','C','C','1']
    ls4 = ['D']
    ls5 = ['D','C','+']
    test = Solution()
    print('output1 is :')
    print('sum:', test.calPoints(ls1))
    print('output2 is :')
    print('sum:', test.calPoints(ls2))
    print('output3 is :')
    print('sum:', test.calPoints(ls3))
    print('output4 is :')
    print('sum:', test.calPoints(ls4))
    print('output5 is :')
    print('sum:', test.calPoints(ls5))
