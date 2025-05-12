
def romanToInt(s):
    maping = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
    total = 0
    prev = 0
    for i in s[::-1]:
        val = maping[i]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

print(romanToInt("LVIII"))