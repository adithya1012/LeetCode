
def decodeString(s):
    stack = []
    cur = ""
    for i in s:
        if i.isdigit():
            if not cur or cur.isdigit():
                cur+=i
            else:
                if stack and str(stack[-1]).isalpha():
                    stack.append(stack.pop() + cur)
                else:
                    stack.append(cur)
                cur = i
        elif i == "[":
            stack.append(int(cur))
            cur = ""
        elif i == "]":
            if cur:
                stack.append(cur)
            val, s_sub = stack.pop(), stack.pop()
            decode_str = val * s_sub
            if stack and str(stack[-1]).isalpha():
                stack.append(stack.pop()+decode_str)
            else:
                stack.append(decode_str)
            cur=""
        else:
            cur+=i
    if cur:
        return "".join(stack)+cur
    else:
        return "".join(stack)

print(decodeString("3[a2[c]]"))