class MinStack:
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));

    # @return nothing
    def pop(self):
        self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]

    def show(self):
        print(self.q)

if __name__ == '__main__':
    test = MinStack()
    test.push(1)
    test.push(2)
    test.push(-2)
    test.show()
    test.pop()
    test.show()
    test.pop()
    test.push(33)
    test.show()
    test.push(-22)
    test.show()
    test.pop()
    test.show()
    test.pop()
    test.show()
    test.pop()
    test.show()

