# Excel Sheet Column Number

def title_number(column_title: str) -> int:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        column_number: int = 0
        for index, letter in enumerate(column_title):
            column_number += ((26 ** (len(column_title) - 1 - index)) * (letters.index(letter) + 1))

        return column_number


inputs = (("A", 1), ("AB", 28), ("BZ", 78), ("ZZ", 702), ("AAC", 705), ("AZA", 1353))

for i in inputs:
    print(i, "\t\t", title_number(i[0]))
