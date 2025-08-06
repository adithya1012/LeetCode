#
# def calculate(s: str) -> int:
#     stack = []
#     num = 0
#     op = "+"
#
#     def helper(op, num):  # Fixed typo: "healper" -> "helper"
#         if op == "+":
#             stack.append(num)
#         elif op == "-":
#             stack.append(-num)
#         elif op == "*":
#             stack.append(stack.pop() * num)
#         else:
#             stack.append(int(stack.pop() / num))
#
#     for i in s:
#         if i.isdigit():
#             num = num * 10 + int(i)
#         elif i in "+-*/()":  # Added condition to skip spaces
#             if i == "(":
#                 stack.append(op)
#                 num = 0
#                 op = "+"
#             elif i == ")":
#                 helper(op, num)  # Fixed typo: "healper" -> "helper"
#                 num = 0
#                 while isinstance(stack[-1], int):
#                     num += stack.pop()
#                 op = stack.pop()  # Fixed: removed helper call, just get the operator
#                 # Don't call helper here, just set num to the result and continue
#                 helper(op, num)  # will be called when we encounter the next operator
#                 num = 0  # Remove this line
#                 op = "+"  # Remove this line
#             else:
#                 helper(op, num)  # Fixed typo: "healper" -> "helper"
#                 op = i
#                 num = 0
#         # print(stack)
#     helper(op, num)  # Fixed typo: "healper" -> "helper"
#     return sum(stack)



def calculate(s: str) -> int:
    num = 0
    op = "+"

    stack = []

    def helper(op, num):
        if op == "+":
            stack.append(num)
        elif op == "-":
            stack.append(-num)
        elif op == "*":
            stack.append(stack.pop() * num)
        elif op == "/":
            stack.append(int(stack.pop() / num))

    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == "(":
            stack.append(op)
            num = 0
            op = "+"
        elif s[i] in ["+", "-", "*", "/", ")"]:
            helper(op, num)
            if s[i] == ")":
                num = 0
                while isinstance(stack[-1], int):
                    num += stack.pop()
                op = stack.pop()
                helper(op, num)
            num = 0
            op = s[i]

    helper(op, num)

    return sum(stack)


print(calculate("2*(5+5*2)/3+(6/2+8)"))