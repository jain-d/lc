# Find Triangular Sum of an Array

def triangular_sum(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    return triangular_sum([(nums[index - 1] + nums[index]) % 10 for index in range(1, len(nums))])


def triangular_sum_2(nums: list[int]) -> int:
    while len(nums) > 1:
        nums = [(nums[index - 1] + nums[index]) % 10 for index in range(1, len(nums))]
    
    return nums[0]


def triangular_sum_3(nums: list[int]) -> int:
    index = 1
    while len(nums) > 1:
        nums[index - 1] = (nums[index - 1] + nums[index]) % 10
        if index == len(nums) - 1:
            nums.pop()
        index = (index + 1) % len(nums)

    return nums[0]


if triangular_sum_3([1, 2, 3, 4, 5]) == 8:
    print("\033[32mPASS\033[0m")
else:
    print("\033[31mFAIL\033[0m")
