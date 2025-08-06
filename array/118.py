# Pascal's Triangle

def generate(num_rows: int) -> list[list[int]]:                 # Bottom Up DP
    triangle: list[list[int]] = []
    for row_number in range(num_rows):
        row: list[int] = []
        for index in range(row_number + 1):
            if index == 0 or index == row_number:
                row.append(1)
            else:
                row.append(triangle[row_number - 1][index - 1] + triangle[row_number - 1][index])
        triangle.append(row)

    return triangle

inputs = ((3, [[1], [1, 1], [1, 2, 1]]), (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]), (1, [[1]]))

for i in inputs:
    if i[1] == (output := generate(i[0])):
        print("\033[1;32mPASS\033[0m")
    else:
        print(f"\n\n\033[1;31mFAIL\033[0m for {i[0]}\noutput={output}, expected={i[1]}\n\n")
