# Excel Sheet Column Title

import string
special_letter = (string.ascii_uppercase.replace("Z", "")).replace("A", "ZA")
special_letters_tuple = tuple(special_letter)

def successive_division(number, divisor) -> list[str]:
    if (not (quotient := number // divisor)) and number:
        return list(special_letters_tuple[number % divisor])
    elif not number:
        return []
    result = successive_division(quotient, divisor) if (remainder := number % divisor) else successive_division(quotient - 1, divisor)
    result.append(special_letters_tuple[remainder])
    return result


def convert_to_title(column_number: int) -> str:
    return "".join(successive_division(column_number, 26))



inputs = ((1, "A"), (26, "Z"), (28, "AB"), (52, "AZ"), (78, "BZ"), (701, "ZY"), (702, "ZZ"), (703, "AAA"), (1378, "AZZ"))

for i in inputs:
    print(i, "\t\t", convert_to_title(i[0]))
