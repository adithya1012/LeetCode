

def encode(strs):
    s = ""
    for i in strs:
        s = s + str(len(i)) + "#" + i
    return s
def decode(s):
    res = []
    while s:
        length = ""
        while s[0] != "#":
            length = length+s[0]
            s = s[1:]
        length_len = len(length)
        length = int(length)
        word = s[1:length+1]
        res.append(word)
        s = s[length+1:]
    return res

s = ["we","say",":","yes","!@#$%^&*()"]

print(decode(encode(s)))
