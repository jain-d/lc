# Isomorphic Strings

def is_isomorphic(s: str, t: str) -> bool:
    mapping_records: dict = {}
    if len(set(s)) != len(set(t)):
        return False
    else:
        for original_letter, replacement in zip(s, t):
            if (pervious_mapping := mapping_records.get(original_letter)):
                if pervious_mapping != replacement:
                    return False
            else:
                mapping_records.update({original_letter: replacement})

    return True



inputs = (("egg", "add"), ("foo", "bar"), ("paper", "title"), ("nasser", "create"))

for i in inputs:
    print(i, '\t\t', is_isomorphic(*i))
