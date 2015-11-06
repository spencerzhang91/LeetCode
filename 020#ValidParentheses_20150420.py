# I omited the class defination on purpose because it's just not necessary at all.
def isvalid(s):
    stack, D = [], {')': '(', ']': '[', '}': '{'}
    for i in range(len(s)):
        if not stack:
            if s[i] in D.keys():
                return False
            else:
                stack.append(s[i])
        elif s[i] in D.keys() and stack[-1] == D[s[i]]:
            stack.pop()
        else:
            stack.append(s[i])
    return True if not stack else False
