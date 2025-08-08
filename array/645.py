# Set Mismatch


def find_error_nums(nums: list[int]) -> list[int]:
    lookup_table = {number: False for number in range(1, len(nums) + 1)}
    extra_number = 0

    for number in nums:
        if number in lookup_table and not lookup_table[number]:
            lookup_table[number] = True
        else:
            extra_number = number

    for key, value in lookup_table.items():
        if not value:
            return [extra_number, key]


inputs = (([1, 2, 2, 4], [2, 3]), ([1, 1], [1, 2]), ([3, 2, 2], [2, 1]))


for i in inputs:
    if i[1] == (result := find_error_nums(i[0])):
        print('\033[1;32mPASS\033[0m')
    else:
        print(f'\033[1;31mFAIL\033[0m\nFor {i}, output = {result}\n\n')

