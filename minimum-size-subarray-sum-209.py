def minSubArrayLen(target, nums):
    sum_val = 0
    min_len = float('inf')  # Use infinity instead of len(nums) + 1
    l = 0

    for r in range(len(nums)):  # Expand the right pointer
        sum_val += nums[r]

        # Shrink the window while sum is greater than or equal to target
        while sum_val >= target:
            min_len = min(min_len, r - l + 1)  # Update min length
            sum_val -= nums[l]  # Shrink the window from the left
            l += 1

    return min_len if min_len != float('inf') else 0  # Return 0 if no valid subarray exists

print(minSubArrayLen(1, [10,9,8,7]))
