# Find the Index of the First Occurrence in a String

def str_str(haystack: str, needle: str) -> int:
    return haystack.find(needle)


inputs = (("sadbutsad", "sad"), ("leetcode", "leeto"))

for i in inputs:
    print(f"{i}\t\t", str_str(*i))

