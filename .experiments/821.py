# Two pass approach for Shortest Distance to a Character

def shortest_to_char(s: str, c: str) -> list[int]:
    character_occurances: list[int] = []
    shortest_distances: list[int]  = []
    for index, letter in enumerate(s):
        if letter == c:
            character_occurances.append(index)

    occurance_lookup = 0
    for index, letter in enumerate(s):
        if letter != c:
            if abs(index - character_occurances[occurance_lookup]) < abs(index - character_occurances[occurance_lookup - 1]):
                shortest_distances.append(abs(index - character_occurances[occurance_lookup]))
        else:
            shortest_distances.append(0)
            occurance_lookup += 1 if occurance_lookup + 1 < len(character_occurances) else 0

    return shortest_distances



inputs = (("loveleetcode", "e"), ("aaab", "b"), ("ffffdffff", "f"), ("aaba", "b"))

for i in inputs:
    print(i, '\t\t\t', shortest_to_char(*i))
