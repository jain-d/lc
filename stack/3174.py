# Clear Digit

def clear_digit(s: str) -> str:
    if len(s) == 1:
        return s
    cleaned: list[str] = []
    for character in s:
        if character.isdigit():
            cleaned.pop()
            continue
        cleaned.append(character)
    
    return "".join(cleaned)


test_cases = (("abc", "abc"), ("cb34", ""), ("x", "x"))

for test_case in test_cases:
    if test_case[1] == clear_digit(test_case[0]):
        print("\033[32mPASS\033[0m")
    else:
        print("\033[31mFAIL\033[0m")

