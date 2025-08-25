# Find the K-Beauty of a Number

def divisor_substrings(num: int, k: int) -> int:
    substrings: int = 0
    string_number = str(num)
    for index in range(len(string_number) - (k - 1)):
        divisor = int(string_number[index:index + k])
        if divisor and not num % divisor:
            substrings += 1

    return substrings


inputs = (((240, 2), 2), ((430043, 2), 2), ((1, 1), 1))

count = 0
for i in inputs:
    if (result := divisor_substrings(*i[0])) == i[1]:
        count += 1
    else:
        print(f"\033[1;31mFAILED\033[0m\nFor {i}, output{result}")

if count == len(inputs):
    print("all test cases \033[32mPASSED\033[0m")
