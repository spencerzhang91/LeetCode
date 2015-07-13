class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.value = []
        self.min = []        

    # @param x, an integer
    # @return an integer
    def push(self, x):
        # print('pushed', x)
        if len(self.value) == 0:
            self.value.append(x)
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)
            self.value.append(x)
        return self.value[-1]     
        
    # @return nothing
    def pop(self):
        if len(self.value) > 0:
            if self.value[len(self.value)-1] == self.min[len(self.min)-1]:
                self.value.pop()
                self.min.pop()
            else:
                self.value.pop()

    # @return an integer
    def top(self):
        if self.value:
            return self.value[-1]
        return None       

    # @return an integer
    def getMin(self):
        if self.min:
            return self.min[-1]
        return None

    # a method for easy testing, omited when submit to OJ
    def show(self):
        print('value:', self.value, ' min:', self.min)

if __name__ == '__main__':
    test = MinStack()
    test.push(2147483646)
    test.push(2147483646)
    test.push(2147483647)
    test.show()
    test.pop()
    test.show()
    test.pop()
    test.show()
    test.pop()
    test.show()
    test.push(2147483647)
    test.show()
    test.push(-2147483648)
    test.show()
    test.pop()
    test.show()

