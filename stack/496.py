# Next Greater Element I
"""
inputs = [4, 1, 2]  [1, 3, 4, 2]

problem -
We get elements in order from array 1, we find their equivalent in array 2, and then we look to the right to find elements bigger than itself here. If we get one, we store that in a new array, or else -1

solution 0-
For every element in first array, we find it's equivalent in second by traversing through the array. Once found, we actively look for the bigger number to the right.
Inefficiency with the solution is that we will be traversing the second array as many times as there are elements in the first. ϴ(n*m) complexity, worst case O(n²).

Instead of traversing every single time, we can create a stack, with the largest element, index values of the largest element.

"""

def solution_one(nums1: list[int], nums2: list[int]) -> list[int]:
    next_greater: list[int] = []
    for number in nums1:
        found = False
        for greater_number in nums2:
            if number == greater_number:
                found = True
            if found and greater_number > number:
                next_greater.append(greater_number)
                found = False
                break
        if found:
            next_greater.append(-1)

    return next_greater


"""
With External Help, an O(n+m) solution
"""

def solution_two(nums1: list[int], nums2: list[int]) -> list[int]:
    the_greatest: list[int] = []
    mapping: dict[int, int] = {}

    for num in nums2:
        if not the_greatest:
            the_greatest.append(num)
            continue

        while the_greatest and num > the_greatest[-1]:
            mapping.update({the_greatest.pop(): num})

        the_greatest.append(num)
    
    return [mapping.get(num, -1) for num in nums1]


inputs = ((([4, 2, 3], [1, 4, 2, 3]), [-1, 3, -1]), (([2, 4], [1, 2, 3, 4]), [3, -1]), (([2, 4, 6, 3, 1], [2, 4, 5, 3, 1, 6]), [4, 5, -1, 6, 6]))

for input in inputs:
    if input[1] == (result := solution_two(*input[0])):
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[31mFAIL\033[0m\nfor {input}, result {result}")
