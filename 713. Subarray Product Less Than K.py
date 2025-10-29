import collections


def numSubarrayProductLessThanK(nums, k):
    left, right = -1, 0
    tmp = collections.deque([])
    res = []
    cur = 1
    if k == 0:
        return []

    while right < len(nums):
        while cur * nums[right] > k:
            left += 1
            cur = cur // nums[left]
            if tmp:
                tmp.popleft()
            if left == right:
                right += 1
                left = right
        cur = cur * nums[right]
        tmp.append(nums[right])
        right += 1
        res.append(list(tmp.copy()))
    return res

print(numSubarrayProductLessThanK([10,5,2,6], 100))
