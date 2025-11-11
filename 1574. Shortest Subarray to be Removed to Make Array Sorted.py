
def findLengthOfShortestSubarray(arr):
    l, r = 1, len(arr)-1
    res = len(arr)
    while l < len(arr):
        if arr[l-1] > arr[l]:
            break
        l += 1
    if l == len(arr):
        return 0
    l -= 1
    print(l)
    res = min(res, r-l)
    while l >= 0:

        while l < r and arr[l] <= arr[r]:
            r -= 1
        res = min(res, r-l)
        l-=1
    return res


print(findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))