# Reverse String II (Iterative Approach)

def rev_str(s: str, k: int) -> str:
    rev_str_list: list[int] = []
    for _ in range(0, len(s), 2*k):
        pass
    return "".join(rev_str_list)


print(rev_str("abcdefg"))