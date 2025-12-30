# Count Prefix and Suffix Pairs I

def count_prefix_suffix_pair(words: list[str]) -> int:
    count: int = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if len(words[i]) <= len(words[j]) and (words[i] == words[j][:len(words[i])] and words[i] == words[j][-len(words[i]):]):
                count += 1

    return count

inputs = ((["a", "aba", "ababa", "aa"], 4), (["pa", "papa", "ma", "mama"], 2), (["abab", "ab"], 0))

for words, result in inputs:
    if (return_val := count_prefix_suffix_pair(words)) == result:
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nfor {words}, expected {result}, returned {return_val}")
