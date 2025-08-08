# Set Mismatch

def find_error_num(nums: list[int]) -> list[int]:
    current_sum = sum(nums)
    duplicate = current_sum - sum(set(nums))
    missing_number = int(((len(nums) * (len(nums) + 1)) / 2) - (current_sum - duplicate))
    
    return [duplicate, missing_number]

print(find_error_num([1, 2, 2, 4]))
