# Implement Stack using Queue
from collections import deque

class MyStack:
    def __init__(self):
        self.fake_stack = deque()

    def push(self, x: int) -> None:
        self.fake_stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self.fake_stack) - 1):
            self.fake_stack.append(self.fake_stack.popleft())
        return self.fake_stack.popleft()

    def top(self) -> int:
        top_most = self.pop()
        self.fake_stack.append(top_most)
        return top_most

    def empty(self) -> bool:
        return len(self.fake_stack) == 0
