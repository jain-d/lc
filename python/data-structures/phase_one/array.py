# 1. Two Sum

"""
The requirement here within the given array, we find and return the indices of the 2 numbers which would form the target number.
It is established that a combination is there.

So a solution to this could be that-
    - we iterate over the elements of the array
    - for every element, we subtract it from the target, and look for the difference in the rest of the array

For this solution, we just need subtraction and iterations. No special data structure, no algorithm. Just subtraction and iteration.
The complexity of this one would be O(n^2).
Best case the 2 numbers are at indices 0 and 1.
Worst case they are at n - 2 and n - 1.

Another solution-
    - we store all the elements in dict(num, index), O(n) time
    - we iterate and check for the diff, worst case another O(n).

in this solution, we are still using subtraction and iteration, but we are also utilizing a special data structure (hash table) to cut down on compute significantly.
"""

# Solution 1
def two_sum(nums: list[int], target: int) -> list[int]:
        for index in range(1, len(nums)):
            req_num = target - nums[index - 1]
            for idx in range(index, len(nums)):
                if nums[idx] == req_num:
                    return [index - 1, idx]

# Solution 2
def two_sum(nums: list[int], target: int) -> list[int]:
    num_dict = {val: index for index, val in enumerate(nums)}
    for index, num in enumerate(nums):
        if (found_at := num_dict.get(target - num, False)) and found_at != index:
            return [found_at, index]
