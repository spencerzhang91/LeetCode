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
                elif token == '/':            # notice: it's correct implementation in python 3
                    try:                      # but leetcode judge is a little different
                        temp = left / right
                    except ZeroDivisionError:
                        return None
                stack.append(temp)
        return stack[0]

# leetcode passable version
class Solution2(object):
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
                    if left * right < 0 and left % right != 0:
                        temp = left / right +1
                    else:
                        temp = left / right
                stack.append(temp)
        return stack.pop()

if __name__ == '__main__':
    exp = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    test = Solution()
    res = test.evalRPN(exp)
    print(res)
