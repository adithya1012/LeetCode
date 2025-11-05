
def removeAnagrams(words):
    duplicated = set()
    res = []
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in duplicated:
            duplicated.add(sorted_word)
            res.append(word)

    return res

print(removeAnagrams(["a","b","a"]))