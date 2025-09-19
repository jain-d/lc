# Min Stack

class MinStack:
    def __init__(self):
        self.min_stack: list[int] = []
        self.min_elements: list[int] = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if not self.min_elements or val <= self.min_elements[-1]:
            self.min_elements.append(val)

    def pop(self) -> int:
        if self.min_stack[-1] == self.min_elements[-1]:
            self.min_elements.pop()
        return self.min_stack.pop()
        
    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_elements[-1]
