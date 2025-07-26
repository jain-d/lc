# Range Addition 2

def max_count(m: int, n: int, ops: list[list[int]]) -> int:
    max_numbers: list[int] = [m, n]
    for operation in ops:
        if max_numbers[0] > operation[0]:
            max_numbers[0] = operation[0]
        if max_numbers[1] > operation[1]:
            max_numbers[1] = operation[1]
    return max_numbers[0] * max_numbers[1]


inputs = ((3, 3, [[2, 2], [3, 3]]), (3, 3, [[2, 2], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [3, 3], [2, 2]]), (3, 3, []), (3, 3, [[3, 3], [2, 3], [2, 2]]), (1, 1, []), (1, 1, [[1, 1]]), (18, 3, [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]))

for i in inputs:
    print(max_count(*i))
