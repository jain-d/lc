# Reverse String II

def reverse_str(s: str, k: int) -> str:
    if len(s) < k:
        return s[-1::-1]
    elif len(s) >= k and len(s) < 2 * k:
        return s[k - 1::-1] + s[k:]
    else:
        return s[k - 1::-1] + s[k:2 * k] + reverse_str(s[2 * k:], k)




inputs = ((("abcdefg", 2), "bacdfeg"), (("abcd", 2), "bacd"), (("abcdefghijk", 4), "dcbaefghkji"), (("abcdefghi", 3), "cbadefihg"))

for i in inputs:
    if i[1] == (result := reverse_str(*i[0])):
        print("\033[1;32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nFor {i},\t{result}")
