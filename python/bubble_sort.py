unsorted = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def bubble_sort(unsorted: list[int]) -> list[int]:
    index = 0
    was_altered = False
    end = len(unsorted) - 1
    while True:
        if index == end:
            if was_altered:
                index = 0
                end -= 1
                was_altered = False
                continue
            break
        if unsorted[index] > unsorted[index + 1]:
            unsorted[index], unsorted[index + 1] = unsorted[index + 1], unsorted[index]
            was_altered = True

        index += 1
    return unsorted



print(unsorted, bubble_sort(unsorted.copy()))
