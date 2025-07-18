# Summary Range

def summary_ranges(nums: list[int]) -> list[str]:
    list_of_ranges: list[str] = []
    previous_number: int = 0
    starting_number: int = 0
    for index, number in enumerate(nums):
        if index == 0:
            starting_number = number
        elif previous_number + 1 != number:
            if starting_number == previous_number:
                list_of_ranges.append(str(starting_number))
            else:
                list_of_ranges.append(f"{starting_number}->{previous_number}")
            starting_number = number

        if index == len(nums) - 1:
            if starting_number == number:
                list_of_ranges.append(str(number))
            else:
                list_of_ranges.append(f"{starting_number}->{number}")

        previous_number = number

    return list_of_ranges


inputs = ([0, 1, 2, 4, 5, 7], [0, 2, 3, 4, 6, 8, 9])

for i in inputs:
    print(i, summary_ranges(i))

