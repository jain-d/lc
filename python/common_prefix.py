# common prefix
import json

def find_prefix(words: list[str]) -> str:
    trie: dict = {}
    prefix: list[str] = []
    for word in words:
        ctrie = trie
        for letter in word:
            if letter not in ctrie:
                ctrie.update({letter: {}})
            ctrie = ctrie.get(letter)
        ctrie.update({"*": True})
    ctrie = trie
    while ctrie.get("*", False):
        if len(ctrie) != 1:
            break

    """
    while True:
        if len(trie) != 1:
            break
        prefix.append()
        """



words = ["flower", "flow", "flu"]

find_prefix(words)
