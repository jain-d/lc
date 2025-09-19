# Simplify Path

def simplify_path(path: str) -> str:
    canonical_path_stack: list[str] = [""]
    for entry in path.split("/"):
        if entry:
            if entry == "..":
                if len(canonical_path_stack) > 1:
                    canonical_path_stack.pop()
            elif entry == ".":
                continue
            else:
                canonical_path_stack.append(entry)
    if len(canonical_path_stack) == 1:
        return "/"
    return "/".join(canonical_path_stack)



test_cases = (("/home/", "/home"), ("/home//foo/", "/home/foo"), ("/home/user/Documents/../Pictures", "/home/user/Pictures"), ("/../", "/"), ("/.../a/../b/c/../d/./", "/.../b/d"))

for test_case in test_cases:
    if test_case[1] == (result := simplify_path(test_case[0])):
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[31mFAIL\033[0m\nfor {test_case}, {result}")
