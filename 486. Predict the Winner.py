def predictTheWinner(nums) -> bool:
    left, right = 0, len(nums) - 1
    player1 = True
    p1_val = 0
    p2_val = 0
    count = {True: p1_val, False: p2_val}
    while left <= right:
        if nums[left] > nums[right]:
            count[player1] += nums[left]
            left += 1
        else:
            count[player1] += nums[right]
            right -= 1
        player1 = not player1
    # print(p1_val, p2_val)
    return count[True] >= count[False]

print(predictTheWinner([1,5,2]))