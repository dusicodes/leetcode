def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # {tea : [eat, tea, ate], nat: [tan, nat], bat: [bat]}
    hg = {}

    # if len(strs) == 0 or len(strs) == 1:
    #     return [strs[0]]

    for word in strs:
        sorted_string = "".join(sorted(word))

        if sorted_string not in hg:
            hg[sorted_string] = [word]
        else:
            hg[sorted_string].append(word)

    return list(hg.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
