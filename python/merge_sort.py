run_cases = [([3, 2, 1], [1, 2, 3]), ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])]

submit_cases = run_cases + [
    ([], []),
    ([7], [7]),
    ([4, -7, 1, 0, 5], [-7, 0, 1, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
]

def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    left_half = unsorted[:len(unsorted)//2]
    right_half = unsorted[len(unsorted) // 2:]

    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    return merge(sorted_left_half, sorted_right_half)


def merge(left, right):             # [5] [4]
    sorted_list: list[int] = []
    left_pointer, right_pointer = 0, 0
    while left_pointer != len(left) or right_pointer != len(right):
        if left_pointer == len(left):
            sorted_list.extend(right[right_pointer:])
            break
        elif right_pointer == len(right):
            sorted_list.extend(left[left_pointer:])
            break
        else:
            if left[left_pointer] < right[right_pointer]:
                sorted_list.append(left[left_pointer])
                left_pointer += 1
            else:
                sorted_list.append(right[right_pointer])
                right_pointer += 1

    return sorted_list


for case in submit_cases:
    if case[1] == merge_sort(case[0]):
        print(f'PASS')
    else:
        print("FAIL")
