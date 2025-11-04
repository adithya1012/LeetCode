def addBinary(a: str, b: str) -> str:
    base = 2
    carry = 0
    a = a[::-1]
    b = b[::-1]
    i, j = 0, 0
    res = ""
    while i < len(a) or j < len(b):
        first = a[i] if i < len(a) else 0
        second = b[j] if i < len(a) else 0
        total = int(first) + int(second) + carry
        if total >= base:
            res += str(total % base)
            carry = 1
        else:
            res += str(total)
            carry = 0
        i += 1
        j += 1
    if carry:
        res += "1"
    return res[::-1]

print(addBinary("11", "1"))