class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zeros = 0
        ones = 0
        prev = 0
        res = 0
        for i in s:
            if i == "0":
                if prev == "0":
                    zeros += 1
                else:
                    zeros = 1
            elif i == "1":
                if prev == "1":
                    ones += 1
                else:
                    ones = 1
            prev = i
            res = max(res, min(ones, zeros)*2)
        return res

print(Solution().countBinarySubstrings("00110011"))
