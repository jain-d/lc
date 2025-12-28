# Maximum Strong Pair XOR I
import math

def maximum_strong_pair(nums: list[int]) -> int:
    max_strong: int = 0
    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[j] >= math.ceil((nums[i] / 2)) and nums[j] <= (2 * nums[i]):
                max_strong = max(max_strong, (nums[i] ^ nums[j]))
    return max_strong

print(maximum_strong_pair([10, 100]))
