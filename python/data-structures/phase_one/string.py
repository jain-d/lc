# 125. Valid Palindrome

"""
So we have a problem here, which requires slight processing and then checking if it is a palindrome.
I can think of 2 ways of solving it.
first, we reconstruct a clean string by iterating through all the characters, adding it to a new string (or list) if they are non-alpha numeric. We then do a check of if new_string == new_string[::-1].
So what is required here is a loop that runs through to create a new string, a list since we can't have incremental string appends, a string in the end, then a reverse string creation, and then lastly check both via [::-1] which again is O(n).
So a series of O(n), which will boil down to just O(n).


Another way I feel of doing this is via 2 independently moving pointers, starting from either end. this would require only one loop, and minimal state (just storing the position of 2 pointers and weather we have to recalibrate). Just smart iteration logic (pointer increments/decrements) with conditionals. No special structure.
"""

# Second solution
def is_palindrome(s: str) -> bool:
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        recalibrate = False
        if not s[left_pointer].isalnum():
            left_pointer += 1
            recalibrate = True
        if not s[right_pointer].isalnum():
            right_pointer -= 1
            recalibrate = True
        if recalibrate:
            continue
        if s[left_pointer].lower() != s[right_pointer].lower():
            return False
        left_pointer += 1
        right_pointer -= 1

    return True
