
def countPrimes(n: int) -> int:
    count = 0
    for i in range(2,n):
        divisible = False
        for j in range(2, i):
            if i % j == 0:
                divisible = True
                break
        if not divisible:
            print(i)
            count += 1
    return count

countPrimes(10)