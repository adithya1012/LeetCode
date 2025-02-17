"""
Textbook problem: count the number of charters together and compress the string.

aabccccaa -> a2b1c3a2

"""

def string_compress(strs):
    compress_str = ""
    char = strs[0]
    count = 1
    for i in range(1, len(strs)):
        if strs[i] == char:
            count += 1
        else:
            compress_str += char+str(count)
            char = strs[i]
            count = 1
    compress_str += char+str(count)

    return compress_str

print(string_compress("aabccccaa"))
# print(string_compress(""))