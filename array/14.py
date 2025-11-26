# Longest Common Prefix

def longest_common_prefix(strs: list[str]) -> str:
    common_prefix: str = ""
    needs_recomp: bool = False
    for index, entry in enumerate(strs):
        if not index:
            common_prefix = entry
        elif len(entry) < len(common_prefix):
            needs_recomp = False if entry == common_prefix[:len(entry)] else True
            if not needs_recomp:
                common_prefix = entry
        elif len(entry) > len(common_prefix):
            needs_recomp = False if entry[:len(common_prefix)] == common_prefix else True
        else:
            needs_recomp = False if entry == common_prefix else True

        while needs_recomp:
            new_size = min(len(entry), len(common_prefix)) - 1
            if new_size:
                if (entry := entry[:new_size]) == (common_prefix := common_prefix[:new_size]):
                    common_prefix = entry[:new_size]
                    needs_recomp = False
            else:
                return ""

    return common_prefix


inputs = ((["flower", "flow", "flight"], "fl"), (["car", "race", "started"], ""), (["flow" , "flu", "fight"], "f"))

for ingres, outgres in inputs:
    if (output := longest_common_prefix(ingres)) == outgres:
        print(f"\033[32mPASS\033[0m")
    else:
        print(f"\033[31mFAIL\033[0m\nfor {ingres}, {outgres}\t{output}")
