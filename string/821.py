# Shortest Distance to a Character

def shortest_to_char(s: str, c: str) -> list[int]:
    explorer, maintainer, iterator = 0, 0, 0
    shortest_distance: list[int] = []

    while iterator < len(s):
        if s[explorer] == c or explorer + 1 == len(s):
            if s[maintainer] != c:
                maintainer = explorer
            elif s[explorer] == c:
                if abs(maintainer - iterator) < abs(explorer - iterator):
                    shortest_distance.append(abs(maintainer - iterator))
                    iterator += 1
                    continue
                else:
                    maintainer = explorer
                    shortest_distance.append(abs(maintainer - iterator))
                    iterator += 1
            else:
                shortest_distance.append(abs(maintainer - iterator))
                iterator += 1


        explorer += 1 if explorer + 1 < len(s) else 0

    return shortest_distance


"""
# Failed solution
def shortest_to_char(s: str, c: str) -> list[int]:
    shortest_distance: list[int] = []
    i, j, k = 0, 0, 0
    while j < len(s):
        if s[k] == c:
            if s[k] != s[i]:
                shortest_distance.append(abs(k - j))
                j += 1
            else:
                if abs(k - j) < abs(i - j):
                    shortest_distance.append(abs(k - j))
                    j += 1
                else:
                    shortest_distance.append(abs(i - j))
                    k = i
                    j += 1
                    i += 1 if i + 1 < len(s) else 0
                    continue

        if s[i] == c:
            if s[k] != c:
                k = i
            else:
                continue
        i += 1 if i + 1 < len(s) else 0

    return shortest_distance
"""


inputs = (("loveleetcode", "e"), ("aaab", "b"), ("ffffdffff", "f"), ("aaba", "b"))

for i in inputs:
    print(i, '\t\t\t', shortest_to_char(*i))


"""
         |
   l o v e l t e 
   ^ ^ ^   ^ ^


   l o v e l t f e


         |
   l o v e l t f k 3
           ^ ^
"""
