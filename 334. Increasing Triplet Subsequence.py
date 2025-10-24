
def increasingTriplet(nums):
    # stack = []
    #
    # def dfs(i):
    #     if i >= len(nums):
    #         return False
    #     if len(stack) == 3:
    #         return True
    #     if dfs(i + 1):
    #         return True
    #     state = False
    #     if nums[i] > stack[-1]:
    #         stack.append(nums[i])
    #         state = dfs(i + 1)
    #         stack.pop()
    #     return state
    # return dfs(0)

    k = 3
    increasing_ele = [float("inf")] * k
    for n in nums:
        for i in range(len(increasing_ele)):
            if increasing_ele[i] >= n:
                increasing_ele[i] = n
                if i == len(increasing_ele) - 1:
                    print(increasing_ele)
                    return True
                break
    return False

    # first, second = float("inf"), float("inf")
    # for i in nums:
    #     if first >= i:
    #         first = i
    #     elif second >= i:
    #         second = i
    #     else:
    #         return True
    # return False

print(increasingTriplet([2,1,5,0,7]))