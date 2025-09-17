# Decode Nested Strings https://www.boot.dev/challenges/71d17349-910f-4fc5-b639-2962a177559e

class Stack:
    def __init__(self):
        self.items: list[int] = []

    def size(self) -> int:
        return len(self.items)

    def push(self, item: str):
        try:
            self.items.append(int(item))
        except:
            raise Exception(f"Only numbers are allowed.")
    
    def pop(self) -> int:
        if self.size() > 0:
            return self.items.pop(-1)
        raise IndexError(f"Can not pop form an empty stack.")
    
    def peek(self) -> int:
        if self.size() > 0:
            return self.items[-1]
        raise IndexError(f"Stack's empty!")

def decode_string(encoded_string: str) -> str:
    stack = Stack()
    decoded_string: list[str] = []
    characters: list[list[str]] = []
    index = 0
    number = []

    while index < len(encoded_string):
        if encoded_string[index].isdigit():
            number.append(encoded_string[index])
        elif encoded_string[index] == "[":
            stack.push("".join(number))
            number.clear()
            characters.append([])
        elif encoded_string[index] == "]":
            decoded_characters = "".join(characters.pop()) * stack.pop()
            if stack.size():
                characters[-1].append(decoded_characters)
            else:
                decoded_string.append(decoded_characters)
        else:
            if stack.size():
                characters[-1].append(encoded_string[index])
            else:
                decoded_string.append(encoded_string[index])
        index += 1

    return "".join(decoded_string)

print(decode_string("13[z]f"))
