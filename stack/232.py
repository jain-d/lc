# Implement Queue using Stacks

class MyQueue:
    def __init__(self):
        self.fake_queue: list[int] = []

    def push(self, x: int) -> None:
        self.fake_queue.append(x)

    def pop(self) -> int:
        temp_stack: list[int] = []
        for _ in range(len(self.fake_queue) - 1):
            temp_stack.append(self.fake_queue.pop())
        to_return = self.fake_queue.pop()
        for _ in range(len(temp_stack)):
            self.fake_queue.append(temp_stack.pop())
        return to_return

    def peek(self) -> int:
        to_return: int = 0
        temp_stack: list[int] = []
        for _ in range(2*len(self.fake_queue)):
            if to_return:
                self.fake_queue.append(temp_stack.pop())
                continue
            if len(self.fake_queue) == 1:
                to_return = self.fake_queue.pop()
                temp_stack.append(to_return)
                continue
            temp_stack.append(self.fake_queue.pop())
        return to_return


    def empty(self) -> bool:
        return len(self.fake_queue) == 0
