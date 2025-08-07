# Word Pattern

def word_pattern(pattern: str, s: str) -> bool:
    word_list = s.split()
    if len(word_list) != len(pattern):
        return False

    mapping = dict()
    reverse_mapping = dict()

    for letter, word in zip(pattern, word_list):
        if (assigned_word := mapping.get(letter)):
            if assigned_word != word:
                return False
        else:
            mapping[letter] = word

        if (assigned_letter := reverse_mapping.get(word)):
            if assigned_letter != letter:
                return False
        else:
            reverse_mapping[word] = letter

    return True



    
inputs = ((("abba", "dog cat cat dog"), True), (("abba", "dog cat cat fish"), False), (("a", "cat"), True), (("a", "cat cat"), False), (("ab", "dog dog"), False))

for i in inputs:
    if i[1] == word_pattern(*i[0]):
          print(f"\033[1;32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nfor {i}\n\n")


