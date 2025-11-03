

def maxIncreasingSubarrays(nums) -> int:
    # prev_len = 0
    cur_len = 1
    res = 0
    till_max = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:  # increasing sequence
            cur_len += 1
        else:

            res = max(res, min(cur_len, till_max))
            res = max(cur_len // 2, res)
            # prev_len = cur_len
            till_max = max(cur_len, till_max)
            cur_len = 1

    # check one last time at end
    # if prev_len:
    res = max(res, min(till_max, cur_len))
    res = max(cur_len//2, res)
    print(res)
    return res

# maxIncreasingSubarrays([2,5,7,8,9, 2,3,4, 3, 2,3,4,5,6,7,1])
# nums = [1, 2, 3, 1, 2, 3, 4, 5]
nums = [5,6,7,1,2,3,4]

maxIncreasingSubarrays(nums)



# maxIncreasingSubarrays([8,-4,-1,16,20])
