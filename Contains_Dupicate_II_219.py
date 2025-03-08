
def containsNearbyDuplicate(nums, k):
    ele = set()
    window = k+1
    for i in range(window):
        if nums[i] in ele :
            return True
        ele.add(nums[i])
    # window+=1
    print(window-k)
    ele.remove(nums[window-k-1])
    while window<len(nums):
        if nums[window] in ele:
            return True
        ele.remove(nums[window - k])
        ele.add(nums[window])
        window+=1

    return False

print(containsNearbyDuplicate([1,2,3,1], 3))