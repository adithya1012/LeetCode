class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        elements = [True] * (maxChoosableInteger)

        def dfs(state):
            if state >= desiredTotal:
                return True

            for i in range(1, len(elements)):
                if elements[i]:
                    if i+1 + state >= desiredTotal:
                        return True
                    else:
                        elements[i] = False
                        if not dfs(state + i+1):
                            # elements[i] = True
                            return True
                        elements[i] = True
            return False
        return dfs(0)

print(Solution().canIWin(2, 4))