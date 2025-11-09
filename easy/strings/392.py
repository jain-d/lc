def isSubsequence(s: str, t: str) -> bool:
    if not s:
        return True
    else:
        positions = []
        for i in s:
            if i in t:
                index = t.index(i)
                if index not in positions:
                    positions.append(index)
            else:
                positions = []
                break

        print(positions)
        if len(positions) > 0 and list(positions) == sorted(list(positions)):
            return True
    return False


s = "b"
t = "abc"

print(isSubsequence(s, t))
