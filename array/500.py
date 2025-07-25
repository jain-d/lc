# Keyboard Row

def find_words(words: list[str]) -> list[str]:
    possible_words: list[str] = []
    keyboard = dict(first_row=set("qwertyuiop"), second_row=set("asdfghjkl"),
                    third_row=set("zxcvbnm"))
    for word in words:
        for rows in keyboard.values():
            if set(word.lower()).issubset(rows):
                possible_words.append(word)
    return possible_words


inputs = (["Hello", "Alaska", "Dad", "Peace"], ["omk"], ["adsdf", "sfd"])

for i in inputs:
    print(i, "\t\t", find_words(i))
