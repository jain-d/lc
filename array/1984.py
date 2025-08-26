# Minimum Difference Between Highest and Lowest of K Scores 

def minimum_difference(nums: list[int], k: int) -> int:
    if k == 1:
        return 0
    nums.sort()
    m = k - 1
    smallest: int = nums[m] - nums[0]
    for index in range(1, len(nums) - m):
        smallest = min(smallest, (nums[index + m] - nums[index]))

    return smallest


inputs = ((([9, 4, 1, 7], 2), 2), (([90], 1), 0), (([4, 2, 1, 3, 4, 2, 3], 2), 0), (([9, 4, 1, 7], 3), 5), (([1, 6, 7, 9], 2), 1))

count = 0
for i in inputs:
    if (result := minimum_difference(*i[0])) == i[1]:
        count += 1
    else:
        print(f"\n\033[1;31mFAILED\033[0m\nFor {i}, output {result}")

if count == len(inputs):
    print("all test cases \033[32mpassed\033[0m.")
