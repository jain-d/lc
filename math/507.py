# Perfect Number

def check_perfect_number(num: int) -> bool:
    if num == 1:
        return False
    sum_of_divisors: int = 1
    for divisor in range(2, round(num**0.5 + 1)):
        if num % divisor == 0:
            sum_of_divisors += divisor + num//divisor

    return sum_of_divisors == num
    

inputs = ((28, True), (7, False), (1, False))

count = 0
for i in inputs:
    if i[1] == check_perfect_number(i[0]):
        count += 1
    else:
        print(f"\033[1;31mFAIL\033[0m\nFor {i}")

if count == len(inputs):
    print("All test cases \033[32mPASSED\033[0m")
