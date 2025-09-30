# Next Greater Element II


# Another Failed solution
def binned_3_next_greater_element(nums: list[int]) -> list[int]:
    mapping: dict[int, int] = {}
    index_stack: list[int] = []
    index = 0

    for index, number in enumerate(nums):
        while index_stack and number > nums[index_stack[-1]]:
            mapping.update({index_stack.pop(): number})
        index_stack.append(index)

    for index in range(len(index_stack) - 1, -1, -1):
        if nums[index_stack[0]] > nums[index_stack[index]]:
            mapping.update({index_stack[index]: nums[index_stack[0]]})
        else:
            mapping.update({index_stack[index]: -1})

    return [mapping[index] for index in range(len(nums))]


def next_greater_element(nums: list[int]) -> list[int]:
    mapping: dict[int, int] = {}
    index_stack: list[int] = []
    index = 0

    while len(mapping) < len(nums):
        if not index_stack and index not in mapping:
            index_stack.append(index)
            index = (index + 1) % len(nums)

        while index_stack and nums[index] >= nums[index_stack[-1]]:
            if nums[index] > nums[index_stack[-1]]:
                mapping.update({index_stack.pop(): nums[index]})
            elif index <= index_stack[-1] and index not in mapping:
                mapping.update({index_stack.pop(): -1})
            else:
                break

        if not index_stack or (index not in mapping and index > index_stack[-1]):
            index_stack.append(index)

        index = (index + 1) % len(nums)

    return [mapping[index] for index in range(len(nums))]


# Failed solution
def binned_next_greater_element(nums: list[int]) -> list[int]:
    next_greater: list[int] = []
    temp_stack: list[int] = []
    number = 0
    while len(next_greater) < len(nums):
        if not temp_stack:
            temp_stack.append(nums[number])
            number = (number + 1) % len(nums)

        while temp_stack and nums[number] > temp_stack[-1]:
            next_greater.append(nums[number])
            temp_stack.pop()

        if temp_stack and nums[number] == temp_stack[-1]:
            next_greater.append(-1)
            temp_stack.pop()
        else:
            temp_stack.append(nums[number])
            
        number = (number + 1) % len(nums)

    return next_greater


inputs = (([6, 7, 4, 3, 2, 5, 4, 6, 5, 7], [7, -1, 5, 5, 5, 6, 6, 7, 7, -1]), ([3, 2, 7, 5, 4, 7, 6, 1], [7, 7, -1, 7, 7, -1, 7, 3]), ([2, 8, 7, 2, 1, 3, 2, 1], [8, -1, 8, 3, 3, 8, 8, 2]), ([6, 7, 5, 7, 4, 7, 3, 7], [7, -1, 7, -1, 7, -1, 7, -1]), ([1,2,3,4,5,6,5,4,5,1,2,3],[2,3,4,5,6,-1,6,5,6,2,3,4]))

for input in inputs:
    if input[1] == (result := next_greater_element(input[0])):
        print('\033[32mPASS\033[0m')
    else:
        print(f'\033[1;31mFAIL\033[0m\nfor {input}, result {result}')
