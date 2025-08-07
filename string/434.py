# Number of Segments in a String

def count_segment(s: str) -> int:
    segments: int = 0
    increment_flag = True
    for character in s:
        if ord(character) != 32 and increment_flag:
            segments += 1
            increment_flag ^= True
        elif ord(character) == 32 and not increment_flag:
            increment_flag ^= True

    return segments


inputs = (("Hello, my name is John", 5), ("", 0), ("hello", 1), (" 1  2   3    ", 3))

for i in inputs:
    if i[1] == count_segment(i[0]):
        print("\033[1;32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nFor {i}\n\n")
