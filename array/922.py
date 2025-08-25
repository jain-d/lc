# Sort Array By Parity II

# first solution
def sort_by_parity(nums: list[int]) -> list[int]:
    sorted_array: list[int] = []
    odd_pointer = 0
    even_pointer = 0
    while len(sorted_array) != len(nums):
        if len(sorted_array) % 2 == 0 and even_pointer < len(nums):
            if nums[even_pointer] % 2 == 0:
                sorted_array.append(nums[even_pointer])
            even_pointer += 1
        else:
            if nums[odd_pointer] % 2 != 0 and odd_pointer < len(nums):
                sorted_array.append(nums[odd_pointer])
            odd_pointer += 1

    return sorted_array



# little optimized solution (still way slower then the fastest 😔)
def sort_by_parity_ii(nums: list[int]) -> list[int]:
    odd_pointers: list[int] = []
    even_pointers: list[int] = []

    for index, value in enumerate(nums):
        if (odd_even := index % 2) != value % 2:
            if odd_even:
                if even_pointers:
                    swap_index = even_pointers.pop()
                    nums[index], nums[swap_index] = nums[swap_index], nums[index]
                    continue
                odd_pointers.append(index)
            else:
                if odd_pointers:
                    swap_index = odd_pointers.pop()
                    nums[index], nums[swap_index] = nums[swap_index], nums[index]
                    continue
                even_pointers.append(index)

    return nums



inputs = (([4, 2, 5, 7], [4, 5, 2, 7]), ([3, 2], [2, 3]), ([4, 7], [4, 7]), ([7, 6, 5, 4, 3, 2], [6, 7, 4, 5, 2, 3]), ([7, 5, 3, 2, 4, 6], [2, 7, 4, 5, 6, 3]))

for i in inputs:
    print("\n\n", i[0])
    print(sort_by_parity_ii(i[0]))

