
def countValidSelections(nums) -> int:
    n = len(nums)
    total = sum(nums)
    prefix_sum = [nums[0]] * (n + 1)
    for i in range(1, n):
        prefix_sum[i+1] = prefix_sum [i] + nums[i]
    print(prefix_sum)
    count = 0
    for i in range(n):
        if nums[i] == 0:
            if prefix_sum[i] == (total - prefix_sum[i]):
                count += 2
            elif prefix_sum[i] == (total - prefix_sum[i] - 1):
                count += 1
            elif prefix_sum[i] - 1 == (total - prefix_sum[i]):
                count += 1

    return count

print(countValidSelections([1,0,2,0,3]))