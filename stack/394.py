# Decode String

def decode_string(encoded_string: str) -> str:
    multiplier_stack: list[int] = []
    decoded_string: list[str] = []
    characters: list[list[str]] = []
    number = []

    for character in encoded_string:
        if character.isdigit():
            number.append(character)
        elif character == "[":
            multiplier_stack.append(int("".join(number)))
            number.clear()
            characters.append([])
        elif character == "]":
            decoded_characters = "".join(characters.pop()) * multiplier_stack.pop()
            if multiplier_stack:
                characters[-1].append(decoded_characters)
            else:
                decoded_string.append(decoded_characters)
        else:
            if multiplier_stack:
                characters[-1].append(character)
            else:
                decoded_string.append(character)

    return "".join(decoded_string)

