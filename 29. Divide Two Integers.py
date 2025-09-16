
def divide(dividend: int, divisor: int) -> int:
    d = abs(dividend)
    dv = abs(divisor)
    res = 0
    while d >= dv:
        tmp = dv
        mul = 1
        while d >= tmp:
            d -= tmp
            res += mul
            mul += mul
            tmp += tmp
        # res += mul
        # d -= tmp
    return res

divide(10,3)