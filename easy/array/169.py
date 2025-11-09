from typing import List


def majorityElement(nums: List[int]) -> int:
    num_counts = {}
    cap = len(nums) // 2

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    for num, count in num_counts.items():
        if count > cap:
            return num

    return


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
