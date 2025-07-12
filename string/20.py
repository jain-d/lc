# Valid Parentheses

def is_valid(s: str) -> bool:
    opening_brackets = {"(", "{", "["}
    bracket_stack: list = []
    for bracket in s:
        if bracket in opening_brackets:
            bracket_stack.append(bracket)
        elif len(bracket_stack):
            if ord(bracket) - ord(bracket_stack[-1]) in {1, 2}:
                bracket_stack.pop()
            else:
             return False
        else:
            return False
    return True if not len(bracket_stack) else False


inputs = ("()", "()[]{}", "(]", "([])", "(){}}{", "(])")

for i in inputs:
    print(f"for {i}", is_valid(i))
