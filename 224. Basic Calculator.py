
def calculate(s) -> int:
    def evaluate(subs):
        tmp = ""
        i = 0
        while i < len(subs):
            if subs[i] == "+" and tmp:
                i += 1
                tmp1 = ""
                while i < len(subs) and subs[i] not in ["+", "-"]:
                    tmp1 += subs[i]
                    i += 1

                tmp = str(int(tmp) + int(tmp1))
            elif subs[i] == "-" and tmp:
                i += 1
                tmp1 = ""
                while i < len(subs) and subs[i] not in ["+", "-"]:
                    tmp1 += subs[i]
                    i += 1
                tmp = str(int(tmp) - int(tmp1))
            else:
                tmp += subs[i]
                i += 1
        return tmp

    stack = []
    for i in s:
        if i:
            if i != ")":
                stack.append(i)
            else:
                subs = ""
                while stack[-1] != "(":
                    subs = stack.pop()+subs
                stack.pop()
                res = evaluate(subs)
                stack.append(res)
    print(stack)
    if len(stack) > 1:
        return int(evaluate("".join(stack)))
    else:
        return int(stack[0])

print(calculate("1-(     -2)"))