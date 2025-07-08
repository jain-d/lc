# Backspace String Compare

def backspace_compare(s: str, t: str) -> bool:
    cleaned_s: list = []
    cleaned_t: list = []
    erase_count = 0
    for character in reversed(s):
        if character == "#":
            erase_count += 1
            continue
        if not erase_count:
            cleaned_s.append(character)
        else:
            erase_count -= 1

    erase_count = 0
    for character in reversed(t):
        if character == "#":
            erase_count += 1
            continue
        if not erase_count:
            cleaned_t.append(character)
        else:
            erase_count -= 1
                
    print(cleaned_s, cleaned_t)
    return "".join(cleaned_t) == "".join(cleaned_s)

print(backspace_compare("a#c", "b"))
