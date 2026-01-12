class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = 0
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                if stack:
                    stack.pop()
                elif stars == 0:
                    return False
                else:
                    stars -= 1
            else:
                stars += 1
        if len(stack) > stars:
            return False
        return True


print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))