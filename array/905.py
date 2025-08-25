# Sort Array By Parity

def sort_array_by_parity(nums: list[int]) -> list[int]:
    sorted_list: list[int] = []
    odd_pointer, even_pointer = 0, 0
    while len(sorted_list) != len(nums):
        if even_pointer < len(nums):
            if (even_number := nums[even_pointer]) % 2 == 0:
                sorted_list.append(even_number)
            even_pointer += 1
        elif odd_pointer < len(nums):
            if (odd_number := nums[odd_pointer]) % 2 != 0:
                sorted_list.append(odd_number)
            odd_pointer += 1

    return sorted_list




inputs = (([3, 1, 2, 4], [2, 4, 3, 1]), ([0], [0]), ([7, 1, 4, 3, 0, 5, 2], [4, 0, 2, 7, 1, 3, 5]))

count = 0
for i in inputs:
    if (output := sort_array_by_parity(i[0])) == i[-1]:
        count += 1
    else:
        print(f"\n\033[1;31mFAIL\033[0m\nFor {i}, output {output}")

if count == len(inputs):
    print("all test cases \033[32mPASSED\033[0m")
