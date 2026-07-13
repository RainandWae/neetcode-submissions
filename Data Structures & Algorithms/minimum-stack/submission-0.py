class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Simple append stack
        self.stack.append(val)

        #minStack
        if self.minStack: # minStack not empty
            val = min(val, self.minStack[-1])
        else:
            val = val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]