# Time Needed to Buy Tickets
from collections import deque

def time_required_to_buy(tickets: list[int], k: int) -> int:
    # queue logic
    second_count = 0
    ticket_queue = deque(tickets)
    while True:
        second_count += 1
        off_the_queue = ticket_queue.popleft()
        if off_the_queue == 1:
            if k == 0:
                return second_count
        else:
            ticket_queue.append(off_the_queue - 1)
            if k == 0:
                k = len(ticket_queue)
        k -= 1



test_cases = ((([5, 1, 1, 1], 0), 8), (([2, 3, 2], 2), 6), (([2, 3, 2], 1), 6))

for test_case in test_cases:
    if test_case[1] == (result := time_required_to_buy(*test_case[0])):
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nfor {test_case}, result {result}")
