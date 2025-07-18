# Plus One
def plus_one(digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        string_digits = [str(digit) for digit in digits]
        number = int("".join(string_digits)) + 1
        new_string_digits = list(str(number))
        new_digits = [int(string_number) for string_number in new_string_digits]

        return new_digits


inputs = ([8], [1, 2, 3], [9], [4, 5, 3, 2, 1], [9, 9], [9, 8, 9])

for i in inputs:
    print(plus_one(i))
    
print("\n\n")

def plus_one_revised(digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            carry: int = 0
            index: int = len(digits) - 1
            
            while index >= 0:
                if index == len(digits) - 1:
                    digits[index] = 0
                    carry += 1
                elif digits[index] + carry == 10:
                    digits[index] = 0
                else:
                    digits[index] += carry
                    carry -= 1 if carry else 0
                index -= 1

            if carry:
                digits.insert(0, carry)
        else:
            digits[-1] += 1

        return digits

inputs = ([8], [1, 2, 3], [9], [4, 5, 3, 2, 1], [9, 9], [9, 8, 9])

for i in inputs:
    print(plus_one_revised(i))
