# Map Sum Pairs

class MapSum:
    def __init__(self):
        self.root: dict = dict()
        self.the_end = "*"

    
    def insert(self, key: str, val: int) -> None:
        main_trie = self.root
        for letter in key:
            if letter not in main_trie:
                main_trie.update({letter: {}})
            main_trie = main_trie[letter]
        main_trie.update({self.the_end: val})


    def sum(self, prefix: str) -> int:
        main_trie = self.root
        weights: list[int] = []
        for letter in prefix:
            if letter not in main_trie:
                return 0
            main_trie = main_trie[letter]
        self._level_crawler(main_trie, weights)

        return sum(weights)

    def _level_crawler(self, current_state: dict, weights: list[int]) -> None:
        for path in current_state:
            if path == self.the_end:
                weights.append(int(current_state[self.the_end]))
            else:
                self._level_crawler(current_state[path], weights)


ops = ((("sum", "app"), 0), (("insert", ["apple", 3]), None), (("sum", "app"), 3), (("insert", ["app", 2]), None), (("sum", "ap"), 5))

map_sum = MapSum()

for (operation, operand), output in ops:
    returned_val: bool | None
    match operation:
        case "insert":
            returned_val = map_sum.insert(*operand)

        case "sum":
            returned_val = map_sum.sum(operand)

        case _:
            print("\033[31mINVALID OPERATION\033[0m,\nTRY AGAIN")
            break

    if returned_val != output:
        print(f"\033[1;31mFAILED\033[0m\nfor \033[33m{operand}\033[0m {operand}\texpected:\033[34m{output}\033[0m - returned: \033[34m{returned_val}\033[0m")
    else:
        print("\033[32mPASS\033[0m")
