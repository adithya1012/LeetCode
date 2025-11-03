import collections


def maximumTotalDamage(power) -> int:
    count = collections.Counter(power)
    count_list = [(key, key*val) for key, val in count.items()]
    count_list.sort()
    dp = {}
    def dfs(i):
        if i >= len(count_list):
            return 0
        if i in dp:
            return dp[i]
        consider = count_list[i][1]
        for  j in range(i+1, len(count_list)):
            if count_list[i][0] < count_list[j][0]-2:
                consider = max(consider, count_list[i][1]+dfs(j))
        skip = dfs(i+1)
        dp[i] = max(skip, consider)
        return max(skip, consider)
    return dfs(0)

print(maximumTotalDamage([1,1,3,4]))
