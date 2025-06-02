
def calculate(s):
    nums = 0
    stack = []
    sign = "+"
    for c in range(len(s)):
        i = s[c]
        if i.isdigit():
            nums = (nums*10)+int(i)
        if i in "+-/*" or c == len(s)-1:
            if sign == "+":
                stack.append(nums)
            elif sign == "-":
                stack.append(-nums)
            elif sign == "*":
                stack[-1] = stack[-1]*nums
            elif sign == "/":
                stack[-1] = stack[-1]//nums
            sign = i
            nums = 0
    return sum(stack)

print(calculate("1-3+2*2"))

