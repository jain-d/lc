# building a trie where all the probable words are matched

class Trie:
    def __init__(self):
        self.root: dict = dict()
        self.the_end = "*"

    def insert(self, word: str) -> None:
        main_trie = self.root
        for letter in word:
            if letter not in main_trie:
                main_trie.update({letter: {}})
            main_trie = main_trie[letter]
        main_trie.update({self.the_end: True})

    def search(self, prefix: str) -> list[str]:
        matches: list[str] = []
        main_trie = self.root
        for letter in prefix:
            if letter not in main_trie:
                return matches
            main_trie = main_trie[letter]
        self._level_crawler(prefix, main_trie, matches)
        return matches

    def _level_crawler(self, prefix: str, current_pos: dict, matches: list[str]):
        for path in current_pos:
            if path == self.the_end:
                matches.append(prefix)
            else:
                self._level_crawler(f"{prefix}{path}", current_pos[path], matches)


    def __str__(self):
        return f"{self.root}"


trie = Trie()

words = ["apple", "apology", "apply", "app", "appear", "aptitude", "approve"]

for word in words:
    trie.insert(word)

print(trie.search("app")) # output is= ['apple', 'apply', 'app', 'appear', 'approve']
