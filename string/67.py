# Add Binary

def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2)).lstrip("0b").removeprefix("0b")

inputs = (("11", "1"), ("1010", "1011"))

for i in inputs:
    print(i, "\t\t", add_binary(*i))
