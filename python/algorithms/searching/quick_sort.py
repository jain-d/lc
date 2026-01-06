run_cases = [
    ([2, 1, 3], 0, 2, [1, 2, 3]),
    ([9, 6, 2, 1, 8, 7], 0, 5, [1, 2, 6, 7, 8, 9]),
]
submit_cases = [
    ([], 0, -1, []),
    ([1], 0, 0, [1]),
    ([1, 2, 3, 4, 5], 0, 4, [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], 0, 4, [1, 2, 3, 4, 5]),
    ([0, 1, 6, 4, 7, 3, 2, 8, 5, -9], 0, 9, [-9, 0, 1, 2, 3, 4, 5, 6, 7, 8]),
]


def quick_sort(nums, low, high):
    if low < high:
        mid: int = partition(nums, low, high)
        quick_sort(nums, low, mid - 1)
        quick_sort(nums, mid + 1, high)


def partition(nums, low, high) -> int:
    i, j = low - 1, low
    pivot = high
    while j <= pivot - 1:
        if nums[j] < nums[pivot]:
            i += 1
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]

        if j == pivot - 1:
            i += 1
            if i != pivot:
                nums[i], nums[pivot] = nums[pivot], nums[i]
            return i

        j += 1


for case in submit_cases:
    quick_sort(case[0], case[1], case[2])
    if case[0] == case[-1]:
        print("\033[32mPASS")
    else:
        print(f"\033[1;31mFAIL\033[0m\nfor {case}")
