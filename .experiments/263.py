# Ugly Number, FASTER

def is_ugly(number: int) -> bool:
    if number > 0:
        if number > 5 and is_prime(number):
            return False
        else:
            factors: list[int] = []
            for divisor in range(2, round(number**0.5 + 1)):
                if number % divisor == 0:
                    factors.extend((divisor, int(number / divisor)))
    return False

def is_prime(number):
    for divisor in range(2, round(number**0.5 + 1)):
        if number % divisor == 0:
            return False
    return True


inputs = ((1, True), (2, True), (3, True), (4, True), (5, True), (6, True), (7, False), (8, True), (9, True), (14, False), (-14, False))

count = 0
for i in inputs:
    if i[1] == is_ugly(i[0]):
        count += 1
    else:
        print(f"\033[1;31mFAIL\033[0m\nFor {i}")

    if count == len(inputs):
        print(f"All test cases \033[32mPASSED\033[0m")
