# Lexicographical Numbers

def lexical_order(n: int) -> list[int]:
    lexi_list: list[int] = []
    for number in range(1, n + 1):
        for times in range(5):


inputs = ((13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]), (2, [1, 2]), (25, [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 3, 4, 5, 6, 7, 8, 9]))

for number, expected_result in inputs:
    if (output := lexical_order(number)) == expected_result:
        print("\033[32mPASS\033[0m")
    else:
        print(f"\n\033[1;31mFAIL\033[0m\nfor {number}\ne: {expected_result}\no: {output}")
