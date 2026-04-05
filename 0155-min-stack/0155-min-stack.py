class MinStack:
    def __init__(self):
        self.stack = [] 
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self):
        if not self.stack and not self.minstack:
            return ("Stack Underflow")
        else:
            self.stack.pop()
            self.minstack.pop()

    def top(self):
        return self.stack[-1]  # last element = top

    def getMin(self):
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()