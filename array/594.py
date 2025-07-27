# Longest Harmonious Subsequence

def find_lhs_optimized(nums: list[int]) -> int:
    numbers = dict()   
    for number in nums:
        if numbers.get(number):
            numbers[number] += 1
            continue
        numbers[number] = 1
    largest = 0
    for value in numbers:
        local_substring = 0
        if numbers.get(value + 1):
            local_substring = numbers[value] + numbers[value + 1]
        if largest < local_substring:
            largest = local_substring
 
    return largest




def find_lhs(nums: list[int]) -> int:
    longest_subsequence = []
    for index, value in enumerate(nums):
        local_longest_subsequence = list((value, ))
        if index + 1 < len(nums):
            for number in nums[index + 1:]:
                if abs(value - number) == 1:
                    local_longest_subsequence.append(number)
                elif number == value and len(local_longest_subsequence) >= 2:
                    local_longest_subsequence.append(number)
        if len(local_longest_subsequence) >= 2 and len(local_longest_subsequence) > len(longest_subsequence):
            longest_subsequence = local_longest_subsequence.copy()
    print(longest_subsequence)
    return len(longest_subsequence)


inputs = ([1, 3, 2, 2, 5, 2, 3, 7], [1, 2, 3, 4], [1, 1, 1, 1], [2, 1, 2], [-3, -1, -1, -1, -3, -2])

for i in inputs:
    print(i, "\t\t", find_lhs_optimized(i))
