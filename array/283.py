# Move Zeros

def move_zeros(nums: list[int]) -> None:
        upper_bound = len(nums)
        index = 0
        while index < upper_bound:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                upper_bound -= 1
                continue
            if nums[upper_bound] == 0:
                upper_bound -= 1

            index += 1

inputs = ([0, 1, 0, 3, 12], [0])

for i in inputs:
    print(i)
    move_zeros(i)
    print(i, '\n\n')
