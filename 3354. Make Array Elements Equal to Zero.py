
def countValidSelections(nums):
    def simulate(i, direction, lst):
        while i < len(lst) and i >= 0:
            if lst[i] != 0:
                break
            if direction == 1:
                i += 1
            else:
                i -= 1
        if i >= len(lst) or i < 0:
            if sum(lst):
                return False
            else:
                return True
        # print(i)
        lst[i] -= 1
        direction = -direction
        i += direction
        return simulate(i, direction, lst)

    count = 0
    for i in range(len(nums)):
        if nums[i] == "0":
            tmp = nums.copy()
            if simulate(i, 1, tmp):
                count += 1
            tmp = nums.copy()
            if simulate(i, -1, tmp):
                count += 1
    return count

print(countValidSelections([1,0,2,0,3]))