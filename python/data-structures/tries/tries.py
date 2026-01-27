# Tries

class Trie:
    def add(self, word):
        trie: dict = self.root
        for letter in word:
            if letter in trie:
                trie = trie[letter]
            else:
                trie.update({letter: {self.end_symbol: True}})
                if trie.get(self.end_symbol):
                    trie.pop(self.end_symbol)
                trie = trie.get(letter)



    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

trie = Trie()
words = ["devs", "devops", "developer"]
for word in words:
    trie.add(word)

print(trie.root)
