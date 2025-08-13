# Faulty Keyboard

def final_string(s: str) -> str:
    word: list[str] = []
    for letter in s:
        if letter == "i":
            word.reverse()
        else:
            word.append(letter)
    return "".join(word)


inputs = (("string", "rtsng"), ("poniiter", "ponter"), ("stressedi", "desserts"))

for i in inputs:
    if i[1] == (result := final_string(i[0])):
        print("\033[1;32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nFor {i},\t{result}")
