
def isHappy(n):
    n = str(n)
    tried = set()
    while n == "1":
        res = 0
        for i in n[::-1]:
            res+=int(i)*int(i)
        n = str(res)
        if n == "1":
            return True
        if n in tried:
            return False
        tried.add(n)
    return n == "1"

print(isHappy(19))