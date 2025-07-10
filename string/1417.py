# Reformat the Sting

def reformat(s: str) -> str:
    letter_list: list = []
    digit_list: list = []
    for character in s:
        if character.isalnum() and character.isalpha():
            letter_list.append(character)
        else:
            digit_list.append(character)

    if len(s) % 2 == 0 and len(letter_list) == len(digit_list):
        reformated_list: list = [letter_list.pop() if index % 2 == 0 else digit_list.pop() for index in range(len(s))]

        return "".join(reformated_list)
    elif (len(s) // 2 == len(letter_list) and len(s) // 2 + 1 == len(digit_list)) or (len(s) // 2 == len(digit_list) and len(s) // 2 + 1 == len(letter_list)):
        if len(s) // 2 == len(letter_list):
            reformated_list: list = [digit_list.pop() if index % 2 == 0 else letter_list.pop() for index in range(len(s))]
        else:
            reformated_list: list = [letter_list.pop() if index % 2 == 0 else digit_list.pop() for index in range(len(s))]

        return "".join(reformated_list)
    else:
        return ""


inputs = ("a0b1c2", "x1yz2d", "a1bc1", "leetcode", "1229857369")

for i in inputs:
    print(i, f"\t\t'{reformat(i)}'")
