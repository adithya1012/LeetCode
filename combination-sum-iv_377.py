def combinationSum4(nums, target):
    dp = {}

    def dfs(total):
        if total == target:
            return 1
        if total > target:
            return 0
        if total in dp:
            return dp[total]

        count = 0
        for num in nums:
            count += dfs(total + num)

        dp[total] = count
        return count

    return dfs(0)


print(combinationSum4([1,2,3], 4))
