
def maximumLength(nums, k):
    dp = {}
    sub = []

    def dfs(i, k):

        if k < 0 or i == len(nums):
            return len(sub)
        if (i, k) in dp:
            return dp[(i, k)]
        val1 = 0
        val2 = dfs(i + 1, k)
        if not sub or nums[i] == sub[-1]:
            sub.append(nums[i])
            val1 = dfs(i + 1, k)
            sub.pop()
        else:
            if k:
                sub.append(nums[i])
                val1 = dfs(i + 1, k - 1)
                sub.pop()


        dp[(i, k)] = max(val1, val2)
        return dp[(i, k)]

    return dfs(0, k)

print(maximumLength([29,30,30], 0))