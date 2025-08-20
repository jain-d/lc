# Ugly Number

def is_ugly(number: int) -> bool:
    if number > 0:
        for divisor in range(2, round(number**0.5 + 1)):
            if number % divisor == 0:
                if divisor > 5 and is_prime(divisor):
                    return False
                elif (quotient := number / divisor) > 5 and is_prime(quotient):
                    return False
        return False if number > 5 and is_prime(number) else True
    else:
        return False


def is_prime(number):
    for divisor in range(2, round(number**0.5 + 1)):
        if number % divisor == 0:
            return False
    return True

inputs = ((9, True), (16, True), (1, True), (15, True), (0, False), (14, False), (6, True), (3, True), (-14, False), (7, False))

for i in inputs:
    if i[1] == is_ugly(i[0]):
        print(f"\033[32mPASS\033[0m")
    else:
        print(f"\033[1;31mFAIL\033[0m\nFor {i}")
