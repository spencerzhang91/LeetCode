class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.data = []
        self.size = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)
        self.size += 1

    # @return nothing
    def pop(self):
        self.data.pop(0)
        self.size -= 1        

    # @return an integer
    def peek(self):
        return self.data[0]

    # @return an boolean
    def empty(self):
        return not bool(self.size)
        
