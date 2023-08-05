#Problem Statement: Design a stack that supports push, pop, top, and retrieving the
# minimum element in constant time.

class MinStack:

    def __init__(self):
        self.list = []
        self.min = []

    def push(self, val: int) -> None:
        self.list.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        res = self.list.pop()
        if res == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min[-1]

minStack = MinStack();
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2