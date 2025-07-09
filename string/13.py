# Roman to Integer

def roman_to_int(s: str) -> int:
    number: int = 0
    lookup_table = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
    potential_subraction_numerals = ("I", "X", "C")
    index = 0
    while index < len(s):
        current_value = lookup_table[s[index]]
        if s[index] in potential_subraction_numerals and index != len(s) - 1:
            if (next_value := lookup_table[s[index + 1]]) == current_value * 5 or next_value == current_value * 10:
                number += next_value - current_value
                index += 2
                continue
            else:
                number += current_value
        else:
            number += current_value
        index += 1

    return number


inputs = ("III", "LVIII", "MCMXCIV", "MDCCCLXXXIV")

for input in inputs:
    print(roman_to_int(input))

