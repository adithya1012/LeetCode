
def jump(nums):
    goal = len(nums) - 1
    res = [float("-inf")] * len(nums)
    res[-1] = 0
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] + i >= goal:
            min_jump = min(res[i+1:i+nums[i]])
            # for j in range(i + 1, goal+1):
            #     if res[j] != -1:
            #         min_jump = min(min_jump, res[j] + 1)

            res[i] = min_jump
            goal = i
    print(res)
    return res[0]

jump([2,3,1,1,4])