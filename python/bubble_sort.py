unsorted = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def original_bubble_sort(unsorted: list[int]) -> list[int]:             # First Principles
    index = 0
    end = len(unsorted) - 1
    was_altered = False
    while True:
        if index == end:
            if was_altered:
                index = 0
                was_altered = False
                continue
            break
        if unsorted[index] > unsorted[index + 1]:
            unsorted[index], unsorted[index + 1] = unsorted[index + 1], unsorted[index]
            was_altered = True
        index += 1

    return unsorted

def refined_bubble_sort(unsorted: list[int]) -> list[int]:
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

def standard_bubble_sort(nums: list[int]) -> list[int]:
    end = len(nums)
    swapping = True

    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1

    return nums

def final_bubble_sort(unsorted: list[int]) -> list[int]:
    index = 1
    end = len(unsorted) - 1
    was_altered = False
    while end > 0:
        if unsorted[index - 1] > unsorted[index]:
            unsorted[index - 1], unsorted[index] = unsorted[index], unsorted[index - 1]
            was_altered = True
        
        if index == end:
            if was_altered:
                index = 1
                end -= 1
                was_altered = False
                continue

        index += 1

    return unsorted

print(unsorted, original_bubble_sort(unsorted.copy()))
