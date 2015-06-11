class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []
        

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.queue.append(x)
        return x
        

    # @return nothing
    def pop(self):
        self.queue.pop()
        

    # @return an integer
    def top(self):
        if len(self.queue) == 0:
            return None
        return self.queue[-1]
        

    # @return an integer
    def getMin(self):
        return min(self.queue)
