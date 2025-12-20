from collections import Counter, defaultdict


class Solution:
    def specialTriplets(self, nums) -> int:
        total_count = Counter(nums)
        cur_count = defaultdict(int)
        res = 0
        for i in nums:
            if i*2 in total_count:
                res += (cur_count[i*2] * (total_count[i*2]-cur_count[i*2]))
            cur_count[i] += 1
        return res

print(Solution().specialTriplets([8,4,2,8,4]))