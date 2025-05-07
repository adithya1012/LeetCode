from collections import defaultdict, Counter
def min_swaps_to_sort_with_zero(arr):
    n = len(arr)
    sorted_arr = sorted([x for x in arr if x != 0]) + [0] * arr.count(0)
    index_map = {val: i for i, val in enumerate(arr)}

    swaps = 0
    arr = arr[:]  # make a copy so we don't modify original
    for i in range(n):
        while arr[i] != sorted_arr[i]:
            if arr[i] == 0:
                target = sorted_arr[i]
                target_idx = index_map[target]
            else:
                target_idx = index_map[0]

            # Swap 0 and the target element
            arr[i], arr[target_idx] = arr[target_idx], arr[i]

            # Update index map
            index_map[arr[target_idx]] = target_idx
            index_map[arr[i]] = i

            swaps += 1

    return swaps

print(min_swaps_to_sort_with_zero([2,3,1,0]))
