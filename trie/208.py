# Implement Trie (Prefix Tree)

class Trie:
    def __init__(self):
        self.root: dict = dict()
        self.this_is_the_end = "*"


    def insert(self, word: str) -> None:
        main_trie = self.root
        for letter in word:
            if letter not in main_trie:
                main_trie.update({letter: dict()})
            main_trie = main_trie[letter]
        main_trie.update({self.this_is_the_end: True})


    def search(self, word: str) -> bool:
        main_trie = self.root
        for letter in word:
            if letter not in main_trie:
                return False
            main_trie = main_trie[letter]

        return True if self.this_is_the_end in main_trie else False


    def startsWith(self, prefix: str) -> bool:
        main_trie = self.root
        for letter in prefix:
            if letter not in main_trie:
                return False
            main_trie = main_trie[letter]

        return True


ops = ((("insert", "apple"), None), (("search", "apple"), True), (("search", "app"), False), (("startsWith", "app"), True), (("insert", "app"), None), (("search", "app"), True))

trie = Trie()

for (operation, operand), output in ops:
    returned_val: bool | None
    match operation:
        case "insert":
            returned_val = trie.insert(operand)

        case "search":
            returned_val = trie.search(operand)
            
        case "startsWith":
            returned_val = trie.startsWith(operand)

        case _:
            print("\033[31mINVALID OPERATION\033[0m,\nTRY AGAIN")
            break

    if returned_val != output:
        print(f"\033[1;31mFAILED\033[0m\nfor \033[33m{operand}\033[0m {operand}\texpected:\033[34m{output}\033[0m - returned: \033[34m{returned_val}\033[0m")
    else:
        print("\033[32mPASS\033[0m")
