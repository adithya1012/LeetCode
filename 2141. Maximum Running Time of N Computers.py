class Solution:
    def maxRunTime(self, n: int, batteries) -> int:
        l, r = 1, sum(batteries)//n
        res = l
        while l<=r:
            target = r - (r-l)//2
            total = 0
            for b in batteries:
               total += min(b, target)
            if total >= n*target:
                res = l
                l = target + 1
            else:
                r = target - 1
        return res


# print(Solution().maxRunTime(2, [1,1,1,1]))