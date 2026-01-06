run_cases = [
    ([5, 3, 8, 6, 1, 9], [1, 3, 5, 6, 8, 9]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
]

submit_cases = run_cases + [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([15, 12, 8, 7, 5, 3, 1], [1, 3, 5, 7, 8, 12, 15]),
    ([10, 5, 3, 7, 2, 8, 1], [1, 2, 3, 5, 7, 8, 10]),
    ([], []),
    ([1], [1]),
]

def selection_sort(nums):
    for index in range(len(nums)):
        smallest_index = index
        for inner_index in range(index + 1, len(nums)):
            if nums[inner_index] < nums[smallest_index]:
                smallest_index = inner_index
        nums[index], nums[smallest_index] = nums[smallest_index], nums[index]
    return nums

for case in submit_cases:
    if case[1] == selection_sort(case[0]):
        print(f"\033[32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nfor {case}")
