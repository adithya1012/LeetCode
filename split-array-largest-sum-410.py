
def splitArray(nums, k):
    l = max(nums)
    r = sum(nums)
    res = float('inf')

    def find_split(capacity):
        total = 0
        split = 0
        max_val = 0
        for i in range(len(nums)):
            total += nums[i]
            if total > capacity:
                max_val = max(max_val, total-nums[i])
                split += 1
                total = nums[i]

        return max(max_val, total), split + 1

    while l <= r:
        m = l + (r - l) // 2
        val, split = find_split(m)
        if split <= k:
            r = m - 1
            res = val
        else:
            l = m + 1
    return res

print(splitArray([20,4,4,7], 3))