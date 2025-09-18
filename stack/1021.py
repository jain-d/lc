# Remove Outermost Parentheses

def remove_outer_parentheses(s: str) -> str:
    primitive_decomp_stack: list[str] = []
    new_strings: list[str] = []
    temp_character_holder: list[str] = []

    for character in s:
        temp_character_holder.append(character)
        if character == "(":
            primitive_decomp_stack.append(character)
        else:
            primitive_decomp_stack.pop()
            if not primitive_decomp_stack:
                new_strings.append("".join(temp_character_holder[1:-1]))
                temp_character_holder.clear()
    return "".join(new_strings)




test_cases = (("(()())(())", "()()()"), ("(()())(())(()(()))", "()()()()(())"), ("()()", ""))

for test_case in test_cases:
    if test_case[1] == (result := remove_outer_parentheses(test_case[0])):
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[31mFAIL\033[0m\nfor {test_case}\tresult = {result}")
