class Solution:
    def maximumProfit(self, prices, k: int) -> int:

        def dfs(i, prev, k):
            if i == len(prices) or k == 0:
                return 0

            if prev > prices[i]:  # we need to buy
                consider = (prev - prices[i]) + dfs(i + 1, prices[i], k - 1)
            else:
                consider = 0
                if i != 0:
                    consider = (prices[i] - prev) + dfs(i + 1, prices[i], k - 1)
            skip = dfs(i + 1, prev, k)

            return max(consider, skip)

        return dfs(0, prices[0], k)

# print(Solution().maximumProfit([1,7,9,8,2], 2))
for i in range(0, 0):
    print(i)