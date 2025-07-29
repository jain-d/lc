# Is Subsequence

def is_subsequence(s: str, t: str) -> bool:
#    substring_indices = []
    past_index = -1
    for letter in s:
        try:
            past_index += t[past_index + 1:].index(letter) + 1
#            substring_indices.append(past_index)
        except ValueError:
#            print(f"\n\nsubstring indices => {substring_indices}")
            return False
#    print(f"\n\nsubstring indices => {substring_indices}")
    return True


inputs = (("abc", "ahbgdc"), ("axc", "ahbcdc"), ("abc", "fcakgctbpaocfet"), ("abc", "ccccccbbbbbbaaaaaa"), ("aaaaa", "baaaa"))

for i in inputs:
    print(i, "\t\t", is_subsequence(*i))


