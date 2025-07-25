# Search Insert Position

def search_insert(nums: list[int], target: int) -> int:
        first: int = 0
        second: int = len(nums) - 1
        while second - first >= 0:
            new_index = (second + first) // 2
            if nums[new_index] == target:
                return new_index
            elif target > nums[new_index]:
                first = new_index
                if second - first <= 1:
                    if nums[second] < target:
                        return second + 1
                    else:
                        return second
            else:
                second = new_index
                if second - first <= 1:
                    if nums[first] < target:
                        return first + 1
                    else:
                        return first





inputs = (([1, 3, 5, 6], 5), ([1, 3, 5, 6], 2), ([1, 3, 5, 6], 7), ([1], 0), ([1], 2), ([1], 1))

for i in inputs:
    print(i, "\t\t", search_insert(*i))
