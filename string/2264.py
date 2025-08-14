# Largest 3-Same-Digit Number in String

def largest_good_integer(nums: str) -> str:
    good_integer = ""
    for i in range(1, len(nums) - 1):
        if nums[i - 1] == nums[i] == nums[i + 1]:
            good_integer = max(good_integer, nums[i])

    return good_integer * 3 if good_integer is not "" else good_integer



inputs = (("6777133339", "777"), ("6222133339888", "888"), ("2300019", "000"), ("4235838824424", ""), ("0003344224424", ""))

for i in inputs:
    if largest_good_integer(i[0]) == i[1]:
        print("\033[1;32mPASS\033[0m")
    else:
        print("\033[1;31mFAIL\033[0m")
