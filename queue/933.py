# Number of Recent Calls
from collections import deque

# Better algorithm
class OptimizedRecentCounter:
    def __init__(self):
        self.request_counter = deque()

    def ping(self, t: int) -> int:
        self.request_counter.append(t)
        while self.request_counter[0] < (t - 3000):
            self.request_counter.popleft()
        return len(self.request_counter)


# Terribly slow original solution
class RecentCounter:
    def __init__(self):
        self.request_counter: list[int] = []

    def ping(self, t: int) -> int:
        self.request_counter.append(t)
        retrival_time = t - 3000

        for index in range(len(self.request_counter)):
            if retrival_time <= self.request_counter[index]:
                break
        
        return (len(self.request_counter) - index)

