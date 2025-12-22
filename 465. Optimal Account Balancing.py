from collections import defaultdict


class Solution:
    def minTransfers(self, transactions) -> int:
        transaction_monitor = defaultdict(int)
        for frm, to, amount in transactions:
            transaction_monitor[frm] -= amount
            transaction_monitor[to] += amount
        print(transaction_monitor)
        balance = [0] * (max(transaction_monitor.keys()) + 1)
        for key, val in transaction_monitor.items():
            balance[key] = val
        print(balance)

        def dfs(i):
            while i < len(balance) and balance[i] == 0:
                i += 1

            if i >= len(balance):
                return 0
            min_transactions = float("inf")
            for j in range(i + 1, len(balance)):
                if balance[i] * balance[j] < 0:
                    balance[j] += balance[i]
                    min_transactions = min(min_transactions, 1 + dfs(i+1))
                    balance[j] -= balance[i]
            return min_transactions

        return dfs(0)



print(Solution().minTransfers([[0,1,1],[1,2,1],[2,3,4],[3,4,5]]))