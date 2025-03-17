def simplifyPath(path):
    path = path.split("/")
    stack = []
    i = 0
    while i < len(path):
        if path[i] == "." or path[i] == "/" or path[i] == "":
            i += 1
            continue
        elif path[i] == "..":
            i += 1
            if stack:
                stack.pop()
        else:
            stack.append(path[i])
            i += 1
    if stack:
        return "/"+"/".join(stack)
    else:
        return "/"

print(simplifyPath("/home//foo/"))