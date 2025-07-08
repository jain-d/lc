# Zigzag Conversion

def convert(s: str, num_row: int) -> str:
    if num_row > 1:
        zigzag_string: list = []
        zigzag_formation: dict = dict()
        for i in range(num_row):
            zigzag_formation[str(i)] = []
        count = 0
        direction = False
        for letter in s:
            print(f"{count} & {letter}")
            zigzag_formation[str(count)].append(letter)
            if count == num_row - 1 or count == 0:
                direction ^= True
            count += 1 if direction else -1
        for letter_list in zigzag_formation.values():
            zigzag_string.extend(letter_list)

        return "".join(zigzag_string)

    return s


#print(convert("PAYPALISHIRING", 3))
print(convert("AB", 1))
