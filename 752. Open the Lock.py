class Solution:
    def openLock(self, deadends, target: str) -> int:
        deadends = set(deadends)
        if target in deadends:
            return -1

        dp = {}

        def dfs(seq):
            if seq == target:
                return 0
            if seq in deadends:
                return float("inf")
            if seq in dp:
                return dp[seq]

            total = float("inf")
            for i in range(len(seq)):
                new_seq = seq[:i] + str((int(seq[i]) + 1) % 10) + seq[i + 1:]
                total = min(total, 1 + dfs(new_seq))
                new_seq = seq[:i] + str((int(seq[i]) - 1) % 10) + seq[i + 1:]
                total = min(total, 1 + dfs(new_seq))
            dp[seq] = total
            return dp[seq]

        return dfs("0000")



# print(Solution().openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))

print(0 % 10)
