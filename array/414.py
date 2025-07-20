# Third Maximum Number

def third_max(nums: list[int]) -> int:
        three_largest: set = set(())
        for number in nums:
            if number not in three_largest:
                if len(three_largest) < 3:
                    three_largest.add(number)
                elif number > min(three_largest) or number > max(three_largest):
                        three_largest.discard(min(three_largest))
                        three_largest.add(number)

        print(f"length of three_largest {len(three_largest)}")
        if len(three_largest) < 3:
            return max(three_largest)
        else:
            return min(three_largest)


inputs = ([3, 2, 1], [1, 2], [2, 2, 3, 1], [1, 7, 1, 7, 1, 7, 7, 1, 7, 1, 1, 1, 7])

for i in inputs:
    print(f"{i}\t", third_max(i))
