# Number of Students Unable to Eat Lunch
from collections import deque

def count_students(students: list[int], sandwiches: list[int]) -> int:
    student_queue = deque(students)
    sandwich_stack = deque(sandwiches)
    mismatch = 0
    
    while mismatch != len(student_queue):
        if student_queue[0] == sandwich_stack[0]:
            student_queue.popleft()
            sandwich_stack.popleft()
            mismatch = 0
        else:
            student_queue.append(student_queue.popleft())
            mismatch += 1

    return len(student_queue)


test_cases = ((([1, 0, 1, 0], [0, 1, 0, 1]), 0), (([1,1,1,0,0,1], [1,0,0,0,1,1]), 3))

for test_case in test_cases:
    if (result := count_students(*test_case[0])) == test_case[1]:
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[31mFAIL\033[0m\nfor {test_case}\tresult = {result}")
