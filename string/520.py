# Detect Capital
from pyutils.colors import Colors

def detect_capital(word: str) -> bool:
    if len(word) == 1:
        return True
    if word[0].isupper():
        return word[1:].islower() or word[1:].isupper()
    else:
        return word[1:].islower()


inputs = (("USA", True), ("FlaG", False), ("leetcode", True), ("Google", True), ("aB", False), ("Ba", True), ("ba", True), ("BA", True), ("a", True))

for i in inputs:
    if i[1] == detect_capital(i[0]):
        print(f"{Colors.GREEN}PASS{Colors.RESET}")
    else:
        print(f"\n\n{Colors.RED}FAIL{Colors.RESET}\nfor {i[0]}\n\n")

    """
    print(i[0], '\t\t', detect_capital(i[0]))
    """
