# Contains Duplicate 2


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    window = set()
    for index, number in enumerate(nums):
        if index > k:
            window.remove(nums[index - k - 1])
        if number in window:
            return True
        
        window.add(number)
    return False


"""
# My failed solution
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    for index, number in enumerate(nums):
        if index + 1 < len(nums) and (occurances := nums[index + 1:].count(number)):
            jump = index + 1
            for _ in range(occurances):
                if abs(index - (nums[jump:].index(number) + jump)) <= k:
                    return True
                jump = nums[jump:].index(number) + jump + 1

    return False
"""

inputs = (([1, 2, 3, 1], 3), ([1, 0, 1, 1], 1), ([1, 2, 3, 1, 2, 3], 2))

for i in inputs:
    print(i, "\t\t", contains_nearby_duplicate(*i))
