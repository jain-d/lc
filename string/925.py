# Long Pressed Name

def is_long_pressed_name(name: str, typed: str) -> bool:
    if name == typed:
        pass
    else:
        name_index, typed_index = 0, 0
        completed = False
        while name_index < len(name) and typed_index < len(typed):
            name_jump, typed_jump = 0, 0
            if typed[typed_index] == name[name_index]:
                further_name_checks, further_typed_checks = 1, 1
                while name_index + further_name_checks <= len(name) - 1 and name[name_index+further_name_checks] == name[name_index]:
                    name_jump += 1
                    further_name_checks += 1
                while typed_index + further_typed_checks <= len(typed) - 1 and typed[typed_index+further_typed_checks] == typed[typed_index]:
                    #print(f"\ntyped-while, for {typed[typed_index]}\n")
                    typed_jump += 1
                    further_typed_checks += 1
                #print(name_jump, typed_jump)
                if not name_jump <= typed_jump:
                    return False
            else:
                return False

            if name_index + name_jump == len(name) - 1 and typed_index + typed_jump == len(typed) - 1:
                completed = not completed

            name_index += name_jump + 1
            typed_index += typed_jump + 1

        if not completed:
            #print(f"failed because of non-completion")
            return False

    return True


print(is_long_pressed_name("saeed", "ssaaedd"))
print(is_long_pressed_name("alex", "aallexx"))
print(is_long_pressed_name("saeed", "ssaaeedd"))

""" Failed Solution 3
def is_long_pressed_name(name: str, typed: str) -> bool:
    if name == typed:
        return True
    else:
        typed_iteration, name_iteration = 0, 0
        while typed_iteration < len(typed):
            jump = 0
            if name_iteration < len(name):
                if typed[typed_iteration] == name[name_iteration]:
                    j = 1
                    while typed_iteration + j < len(typed) and typed[typed_iteration+j] == typed[typed_iteration]:
                        jump += 1
                        j += 1
                    if jump:
                        pass
                else:
                    return False
                typed_iteration += jump + 1 or 1
                name_iteration += 1
            else:
                return False
    return True


print(is_long_pressed_name("saeed", "ssaaedd"))
print(is_long_pressed_name("alex", "aallexx"))
"""

""" Failed Solution 2
def is_long_pressed_name(name: str, typed: str) -> bool:
    if name == typed:
        return True
    else:
        jump = 0
        for index, letter in enumerate(name):
            if name.index(letter) + jump == (index_in_typed := typed.index(letter, index)):
                i = 1
                while index_in_typed + i <= len(typed) - 1 and typed[index_in_typed+i] == letter:
                    jump += 1
                    i += 1
                else:
                    if index + 1 < len(name):
                        continue
                    else:
                        return False


    return True


print(is_long_pressed_name("alex", "aaleexa"))
print(is_long_pressed_name("alex", "aallexx"))
"""

""" Failed solution
def isLongPressedName(name: str, typed: str) -> bool:
    if name == typed:
        return True
    else:
        jump = 0
        for i, letter in enumerate(name):
            if letter in typed:
                if name.count(letter) < typed.count(letter):
                    if name.index(letter, i) + jump == typed.index(letter, i) and i == name.index(letter):
                        jump += typed.count(letter) - name.count(letter)
                elif name.count(letter) == typed.count(letter):
                    if name.index(letter, i) + jump == typed.index(letter, i):
                        pass
                    else:
                        print(f"{typed} failed for letter {letter} at the index + jump of the elif")
                        return False
                else:
                    print(f"{typed} failed at for letter {letter}")
                    return False
            else:
                print(f"{typed} failed at for letter {letter}")
                return False

    return True


print(isLongPressedName("alex", "aaleexa"))
"""

""" ADHD brain, wanting to experiment a better version of set(name), where only consecutive duplicates are removed.
def process_name(name: str):
    list_of_letters: list = []
    iterations = len(name)
    index = 0

    while index < iterations:
        jump = 1
        current_letter = name[index]
        list_of_letters.append(current_letter)
        if (occurances := name.count(current_letter)) > 1:
            for time in range(1, occurances):
                if name[index] == name[index + time]:
                    jump += 1
                else:
                    break
        index += jump
    
    return "".join(list_of_letters)

print(process_name("aalleexx"))
print(process_name("abigail"))
"""
