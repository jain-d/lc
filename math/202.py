# Happy Number

def is_happy(number: int) -> bool:
    computed_values = set()
    while True:
        digits: list[int] = []
        while number > 0:
            digits.append((number % 10)**2)
            number //= 10

        if (total := sum(digits)) == 1:
            return True
        elif total in computed_values:
            return False
        else:
            number = total
            computed_values.add(total)


inputs = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 68, 69, 79, 89, 82, 101, 121, 130, 256, 321)

for i in inputs:
    result = is_happy(i)

    if result:
        print(i, "\t\033[1;32mTrue\033[0m")
    else:
        print(i, "\t\033[1;31mFalse\033[0m")
