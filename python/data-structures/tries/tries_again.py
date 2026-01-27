import json

inputs = ["hello", "help", "hi"]

class Tries:
    def __init__(self):
        self.main_trie = dict()

    def add(self, value: str):
        trie = self.main_trie
        for letter in value:
            if letter.lower() not in trie:
                trie.update({letter: {}})
            trie = trie[letter.lower()]
        trie.update({"*": True})       

    def __str__(self) -> str:
        return f"{self.main_trie}"

    def search(self, value) -> bool:
        trie = self.main_trie
        for letter in value:
            if letter.lower() not in trie:
                return False
            trie = trie[letter.lower()]
        return True

my_trie = Tries()

for ip in inputs:
    my_trie.add(ip)

print(json.dumps(my_trie.main_trie))

#print(my_trie.search("DEVi"))
