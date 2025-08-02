# Valid Anagram
from pyutils.colors import Colors


"""
# first solution
def is_valid(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = dict()
    t_dict = dict()

    for s_letter, t_letter in zip(s, t):
        if s_letter != t_letter:
            if s_dict.get(s_letter):
                s_dict[s_letter] -= 1
            elif t_dict.get(s_letter):
                t_dict[s_letter] += 1
            else:
                t_dict[s_letter] = 1

            if t_dict.get(t_letter):
                t_dict[t_letter] -= 1
            elif s_dict.get(t_letter):
                s_dict[t_letter] += 1
            else:
                s_dict[t_letter] = 1

            if s_dict.get(s_letter) == 0:
                s_dict.pop(s_letter)

            if t_dict.get(t_letter) == 0:
                t_dict.pop(t_letter)

    if len(s_dict) == len(t_dict) == 0:
        return True
    return False
"""


# second solution
def is_valid(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    one_dict = dict()
    for s_letter, t_letter in zip(s, t):
        if s_letter != t_letter:
            if one_dict.get(s_letter):
                one_dict[s_letter] += 1
            else:
                one_dict[s_letter] = 1

            if one_dict.get(t_letter):
                one_dict[t_letter] -= 1
            else:
                one_dict[t_letter] = -1

    for value in one_dict.values():
        if value != 0:
            return False

    return True



inputs = ((("nagaram", "maragan"), True), (("rat", "cat"), False), (("aabb", "baba"), True), (("a", "ab"), False))

for i in inputs:
    if i[1] == is_valid(*i[0]):
        print(f"{Colors.GREEN}PASS")
    else:
        print(f"{Colors.RED}FAIL{Colors.RESET}\nfor {i[0]}")
