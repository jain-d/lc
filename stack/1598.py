
def min_operations(logs: list[str]) -> int:
    where_we_at: list[str] = []
    for op in logs:
        if op == "../":
            if where_we_at:
                where_we_at.pop()
        elif op == "./":
            pass
        else:
            where_we_at.append(op)
    return len(where_we_at)


test_cases = ((["d1/","d2/","../","d21/","./"], 2), (["d1/","d2/","./","d3/","../","d31/"], 3), (["d1/","../","../","../"], 0))

for test_case in test_cases:
    if test_case[1] == (result := min_operations(test_case[0])):
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[31mFAIL\033[0mfor {test_case}, result {result}")
