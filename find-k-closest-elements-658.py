def findClosestElements(arr,k,x):
    diff_arr = [abs(i - x) for i in arr]
    i, j = 0, 0
    ri, rj = 0, 0
    sum_val = 0
    min_sum = float('inf')
    while j < len(arr):
        if j < k:
            sum_val += diff_arr[j]
            ri, rj = i, j
            j += 1
        else:
            if min_sum > sum_val:
                ri, rj = i, j - 1
                min_sum = sum_val
            sum_val -= diff_arr[i]
            i += 1
            sum_val += diff_arr[j]
            j += 1
    return arr[ri:rj + 1]

print(findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9))