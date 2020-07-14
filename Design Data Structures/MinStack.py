class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.curr_min = float('inf')

    def push(self, x: int) -> None:
        if self.curr_min > x:
            self.min_stack.append([x, x])
            self.curr_min = x
        else:
            self.min_stack.append([x, self.curr_min])

    def pop(self) -> None:
        if self.min_stack:
            self.min_stack.pop(-1)
            if not self.min_stack:
                self.curr_min = float('inf')
            else:
                self.curr_min = self.getMin()

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
