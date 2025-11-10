def grayCode(n):
    res = [0]
    for i in range(1, n + 1):
        res = [j + i for j in res[::-1]]
    return res

print(grayCode(2))