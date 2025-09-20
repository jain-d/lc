# First Unique Character in a String

def first_unique_char(s: str) -> int:
    character_dict: dict[str, int] = dict()
    for index, character in enumerate(s):
        if character in character_dict:
            character_dict[character] = -1
        else:
            character_dict.update({character: index})
    for value in character_dict.values():
        if value > -1:
            return value
    return -1

test_cases = (("leetcode", 0), ("loveleetcode", 2), ("aabb", -1), ("abcbc", 0), ("abcba", 2), ("ababab", -1))

for test_case in test_cases:
    if test_case[1] == (result := first_unique_char(test_case[0])):
        print('\033[1;32mPASS\033[0m')
    else:
        print(f"\033[1;31mFAIL\033[0m\nfor {test_case}, result {result}")
