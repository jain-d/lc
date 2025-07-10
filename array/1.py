# Two Sum

def two_sum(nums: list[int], target: int) -> list[int]:

    for index, number in enumerate(nums):
        if nums[index + 1:].count(target - number):
            return [index, nums.index(target - number, index + 1)]

inputs = ([[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6])

for entry in inputs:
    print(two_sum(entry[0], entry[1]))

