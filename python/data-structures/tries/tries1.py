breaking = '\033[31mbreaking\033[0m'
class Trie:
    def longest_common_prefix(self):
        prefix_letter_list: list[str] = []
        main_trie = self.root
        while len(main_trie) == 1 and self.end_symbol not in main_trie:
            letter = list(main_trie.keys())[0]
            prefix_letter_list.append(letter)
            main_trie = main_trie[letter]
        return "".join(prefix_letter_list)

    def advanced_find_matches(self, document, variations):
        matches: set = set()
        for o_index in range(len(document)):
            main_trie = self.root
            for i_index in range(o_index, len(document)):
                if (letter := document[i_index]) in main_trie:
                    main_trie = main_trie[letter]
                elif letter in variations and variations[letter] in main_trie:
                    main_trie = main_trie[variations[letter]]
                else:
                    break

                if self.end_symbol in main_trie:
                    matches.add(document[o_index : i_index+1])
                    break
        return matches

    def find_matches(self, document) -> set:
        bad_words: set = set()
        for o_index in range(len(document)):
            main_trie = self.root
            for i_index in range(o_index, len(document)):
                if document[i_index] not in main_trie:
                    break
                main_trie = main_trie[document[i_index]]
                if self.end_symbol in main_trie:
                    bad_words.add(document[o_index:i_index+1])
                    break
        return bad_words

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True

    def __str__(self):
        return f"{self.root}"

trie = Trie()
for word in ["darn", "heck"]:
    trie.add(word)

#print(json.dumps(trie.root))
#print(trie.longest_common_prefix())

print(trie.advanced_find_matches("d@ng it to h3ck", {"@": "a", "1": "i", "3": "e", "!": "i"}))
