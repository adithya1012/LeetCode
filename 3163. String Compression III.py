
def compressedString(word: str) -> str:
    res = ""
    i = 0
    while i < len(word):
        print(i)
        char = word[i]
        count = 1
        while i+1 < len(word) and word[i] == word[i+1]:
            count += 1
            i += 1
        i+=1
        if count > 9:
            rep = count//9
            for i in range(rep):
                res += "9"+char
            if count%9:
                res += str(count%9) +char
        else:
            res += str(count)+char
    return res

print(compressedString("aaaaaaaaaaaaaabb"))