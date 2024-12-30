class MinStack:

    def __init__(self):
        self.s = []
        self.mins = []

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.mins.append(val)
        elif val <= self.mins[-1]:
            self.mins.append(val)

        self.s.append(val)

    def pop(self) -> None:
        if self.s[-1] == self.mins[-1]:
            self.mins = self.mins[0:len(self.mins)-1]
        self.s = self.s[0:len(self.s)-1]

    def top(self) -> int:
        return self.s[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
