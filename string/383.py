# Ransom Note

def can_construct(ransom_note: str, magazine: str) -> bool:
    lookup_dict: dict[str, int] = dict()
    for letter in magazine:
        if letter in lookup_dict:
            lookup_dict[letter] += 1
        else:
            lookup_dict[letter] = 1

    for letter in ransom_note:
        if letter in lookup_dict:
            lookup_dict[letter] -= 1
        else:
            return False

        if lookup_dict[letter] == 0:
            lookup_dict.pop(letter)

    return True


inputs = ((("a", "b"), False), (("aa", "ab"), False), (("aa", "aab"), True), (("ftp", "fatbpc"), True))

for ip in inputs:
    print("\033[32mPASS\033[0m") if can_construct(*ip[0]) == ip[1] else print("\033[31mFAIL\033[0m")
