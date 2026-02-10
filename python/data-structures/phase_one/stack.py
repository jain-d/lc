# 20. Valid Parentheses

"""
This problem is a template stack problem. You keep stacking opening brackets and then in LIFO order keep close/popping it off.
To solve this, we use a list, which we use as a stack, to append or pop elements.
if a bracket is an openning bracket, we simply append. If a bracket is a closing one, we check what was the last bracket that is in the list. if it is the opening bracket of the same kind, we pop it off.

The Basic things that I have used here is a dictionary that holds the pair information. The closing pair is the key, and the opening pair is the value.
And we have used a python list as a stack here.
Next we traverse through the elements in the string, we check if the element is in the dict (thereby checking if it is closing bracket).
If the element is not a closing bracket, we simply append it in the stack.
If the element is a closing bracket, we first check weather our stack is empty or not. If it is empty, we simply exit.
If it not empty, we check if the last element is matching the opening pair, which we fetch from current elements mapping.

Lastly we check if stack is empty of it has some values.

Both mapping and a list/stack were required here. And a single pass through the passed in string did the job.
Single pass, with special data structures as storage cracked the problem.
""" 

def valid_parentheses(s: str) -> bool:
    closing_pairs = {"}": "{", ")": "(", "]": "["}
    stack: list[str] = []

    for bracket in s:
        if bracket not in closing_pairs:
            stack.append(bracket)
        elif not stack or closing_pairs.get(bracket) != stack[-1]:
            return False
        else:
            stack.pop()
    
    return False if stack else True
