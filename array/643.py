# Maximum Average Subarray 1

def find_max_average(nums: list[int], k: int) -> float:
    max_average: float = float("-inf")
    average: float = 0.00
    for index, number in enumerate(nums):
        if index + 1 < k:
            average += number
        elif index + 1 == k:
            average += number
            average /= k
        else:
            average += (number - nums[index - k]) / k

        if average > max_average and index + 1 >= k:
            max_average = average

    return max_average


inputs = (([1, 12, -5, -6, 50, 3], 4), ([5], 1), ([0, 4, 0, 3, 2], 1))

for i in inputs:
    print(i, "\t\t", find_max_average(*i))
