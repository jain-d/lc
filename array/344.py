# Reverse String

def reverse_string(s: list[str]) -> None:
    first_pointer = 0
    second_pointer = len(s) - 1
    while second_pointer > first_pointer:
        s[first_pointer] = chr(ord(s[first_pointer]) ^ ord(s[second_pointer]))
        s[second_pointer] = chr(ord(s[second_pointer]) ^ ord(s[first_pointer]))
        s[first_pointer] = chr(ord(s[first_pointer]) ^ ord(s[second_pointer]))
        first_pointer += 1
        second_pointer -= 1



inputs = ((["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]), (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]), (["a"], ["a"]))

for i in inputs:
    reverse_string(i[0])
    if i[1] == i[0]:
        print("\033[1;32mPASS\033[0m")
    else:
        print("\033[1;31mFAIL\033[0m")
