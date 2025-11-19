class Solution:
    def wordBreak(self, s: str, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)


print(Solution().wordBreak(s = "leetcodee", wordDict = ["leet","code"]))