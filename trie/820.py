# Short Encoding of Words

def minimum_length_encoding(words: list[str]) -> int:
    count: int = 0
    main_trie: dict = dict()

    for pos, word in enumerate(words):
        trie = main_trie
        increment = 0
        for index in range(len(word) - 1, -1, -1):
            if word[index] not in trie:
                if "*" in trie:
                    increment = index + 1
                    trie.pop("*")
                elif len(trie) > 0:
                    increment = len(word) + 1
                trie.update({word[index]: {}})
            trie = trie[word[index]]
        count += increment if pos else len(word) + 1
        if not pos or increment:
            trie.update({"*": True})

    return count


inputs = ((["time", "me", "bell"], 10), (["t"], 2), (["atime", "time", "ctime"], 12))

for words, answer in inputs:
    if (output := minimum_length_encoding(words)) == answer:
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nw: {words}, exp: {answer}, o/p: {output}")
