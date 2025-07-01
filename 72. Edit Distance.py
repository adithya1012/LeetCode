def minDistance(word1: str, word2: str) -> int:
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)

    def dfs(i, j):
        if i == len(word1) and j == len(word1):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        if word1[i] == word2[j]:
            return dfs(i + 1, j + 1)
        else:
            return 1 + min(dfs(i, j + 1), dfs(i + 1, j + 1), dfs(i + 1, j))

    return dfs(0, 0)

print(minDistance("a", "ab"))