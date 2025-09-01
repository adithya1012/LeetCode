
def calculate(s: str) -> int:
    s = s.strip()
    i = 0
    stack = []
    num = 0
    sign = "+"
    if s[0] in "-":
        sign = "-"
    while i < len(s):
        c = s[i]
        if c.isdigit():
            num = num*10 + int(c)
        if c in "+-*/" or i == len(s)-1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop()*num)
            else:
                stack.append(int(stack.pop()/num))
            sign = c
            num = 0
        i += 1
    return sum(stack)

print(calculate("3*2+2"))