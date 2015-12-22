# 150 Evaluate Reverse Polish Notation

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens: return None
        left = right = None
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    temp = left + right
                elif token == '-':
                    temp = left - right
                elif token == '*':
                    temp = left * right
                elif token == '/':
                    try:
                        temp = left / right
                    except ZeroDivisionError:
                        return None
                stack.append(temp)
        return stack[0]

if __name__ == '__main__':
    exp = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    test = Solution()
    res = test.evalRPN(exp)
    print(res)
