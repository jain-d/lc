# Valid Palindrome

def is_palindrome(s: str) -> bool:
    left_end, right_end = 0, len(s) - 1
    while left_end < right_end:
        if not s[left_end].isalnum():
            left_end += 1
            continue
        elif not s[right_end].isalnum():
            right_end -= 1
            continue
        if s[left_end].lower() == s[right_end].lower():
            left_end += 1
            right_end -= 1
        else:
            return False
    return True



print(is_palindrome("Was it a car or a cat I saw?"))
