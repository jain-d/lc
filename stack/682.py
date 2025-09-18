# Baseball Game

def cal_points(operations: list[str]) -> int:
    results: list[int] = []
    for operation in operations:
        if operation.isdigit() or operation.lstrip("-").isdigit():
            results.append(int(operation))
        elif operation == "D":
            results.append(results[-1]*2)
        elif operation == "C":
            results.pop()
        else:
            results.append(results[-1] + results[-2])

    return sum(results)



test_cases = ((["5","2","C","D","+"], 30), (["5","-2","4","C","D","9","+","+"], 27), (["1", "C"], 0))

for test_case in test_cases:
    if test_case[1] == (result := cal_points(test_case[0])):
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[31mFAIL\033[0m\nfor {test_case}, result = {result}")
