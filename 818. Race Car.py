class Solution:
    def racecar(self, target: int) -> int:

        def dfs(pos, speed):
            if pos < 1:
                return float("inf")
            if pos == target:
                return 0

            if pos < target:
                # Acc
                acc = 1 + dfs(pos + speed, speed * 2)
            # Rev
            if speed > 0:
                rev = 1 + dfs(pos, -1)
            else:
                rev = 1 + dfs(pos, 1)
            return min(acc, rev)

        return dfs(0, 1)



