# Replace Words
def replaceWords(dictionary: list[str], sentence: str) -> str:
    main_trie: dict = dict()
    new_sentence: list[str] = []
    for word in dictionary:
        trie = main_trie
        for letter in word:
            if letter not in trie:
                trie.update({letter: {}})
            trie = trie[letter]
        trie.update({"*": True})

    for count, word in enumerate(sentence.split(), 1):
        trie = main_trie
        for letter_index in range(len(word)):
            if "*" in trie:
                new_sentence.append(word[:letter_index])
                break
            elif word[letter_index] not in trie:
                new_sentence.append(word)
                break
            trie = trie[word[letter_index]]
        if len(new_sentence) != count:
            new_sentence.append(word)


    return " ".join(new_sentence)


inputs = (([["cat", "bat", "rat"], "the cattle was rattled by the battery"], "the cat was rat by the bat"), ([["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"], "a a b c"), ([["fat", "name"], "the fatty cow named fa"], "the fat cow name fa"))

for args, expected_output in inputs:
    if (actual_output := replaceWords(*args)) == expected_output:
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nexpected:\t{expected_output}\nactual:\t{actual_output}\n")
