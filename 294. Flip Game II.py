class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}

        def dfs(state: str) -> bool:
            if state in memo:
                return memo[state]

            for i in range(len(state) - 1):
                if state[i] == '+' and state[i + 1] == '+':
                    next_state = state[:i] + "--" + state[i + 2:]
                    if not dfs(next_state):
                        # this is where we are asking the next player to play (optimally).
                        # Now the next player return False means he can never win. Which mean i am winning.
                        # When i am winning i will return True. I just wanted to make sure that next playing is failing with this state.
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        return dfs(currentState)

print(Solution().canWin("++++"))
