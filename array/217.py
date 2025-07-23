# Contains Duplicate


def contains_duplicate2(nums: list[int]) -> bool:
    new_set = set()
    for number in nums:
        if number in new_set:
            return True
        else:
            new_set.add(number)
    return False





def contains_duplicate(nums: list[int]) -> bool:
    if len(set(nums)) < len(nums):
        return True
    return False

inputs = ([1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

for i in inputs:
    print(i, '\t\t', contains_duplicate2(i))
