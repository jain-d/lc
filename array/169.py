# Majority Element


"""
# Failed Experiment
def majority_element(nums: list[int]) -> int:
    first, second = 0, len(nums) - 1
    element_dict = dict()
    most_appearances = 0

    while second >= first:
        if second != first:
            if nums[second] == nums[first]:
                if not element_dict.get(nums[first]):
                    element_dict[nums[first]] = 2
                else:
                    element_dict[nums[first]] += 2

                if element_dict[nums[first]] > len(nums) // 2:
                    most_appearances = first
                    first += 1
                    second -= 1
                    continue
            else:
                if not element_dict.get(nums[first]):
                    element_dict[nums[first]] = 1
                else:
                    element_dict[nums[first]] += 1

        if not element_dict.get(nums[second]):
            element_dict[nums[second]] = 1
        else:
            element_dict[nums[second]] += 1

        if element_dict[nums[first]] > len(nums) // 2:
            most_appearances = nums[first]
        elif element_dict[nums[second]] > len(nums) // 2:
            most_appearances = nums[second]

        first += 1
        second -= 1

    return most_appearances
"""

def majority_element(nums: list[int]) -> int:
    element_dictionary = dict()
    majority_element = 0
    for number in nums:
        if not element_dictionary.get(number):
            element_dictionary[number] = 1
        else:
            element_dictionary[number] += 1

        if element_dictionary[number] > len(nums) // 2:
            majority_element = number

    return majority_element

inputs = ([3, 2, 3], [2, 2, 1, 1, 1, 2, 2])

for i in inputs:
    print(i, '\t\t\t', majority_element(i))
