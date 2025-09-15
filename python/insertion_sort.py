run_cases = [([4, 3, 2, 1], [1, 2, 3, 4]), ([9, 5, -3, 7], [-3, 5, 7, 9])]

submit_cases = [
    ([], []),
    ([1], [1]),
    ([5, 3, 4, 1, 2], [1, 2, 3, 4, 5]),
    ([0, -2, -5, 3, 2, 1], [-5, -2, 0, 1, 2, 3]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
]


def insertion_sort(unsorted: list[int]) -> list[int]:
    if len(unsorted) > 1:
        tracker, swapper = 1, 1
        while tracker < len(unsorted):
            if unsorted[swapper - 1] > unsorted[swapper]:
                while swapper > 0:
                    if unsorted[swapper - 1] <= unsorted[swapper]:
                        break
                    unsorted[swapper - 1], unsorted[swapper] = unsorted[swapper], unsorted[swapper - 1]
                    swapper -= 1
            tracker += 1
            swapper = tracker
    return unsorted



for case in submit_cases:
    if case[1] == (received := insertion_sort(case[0])):
        print('\033[32mPASS\033[0m')
    else:
        print(f"\033[1;31mFAIL\033[0m\n,for {case}, received {received}")
