
# https://chatgpt.com/c/696496c3-9a54-8332-8c84-314920d12d26


import bisect
# a = [[1,5],[2,1],[3,2],[4,1],[4,1],[4,1],[4,1],[4,3],[5,1]]

a = [0,1,2,3,5]


# bisect.insort_right(a, 5)
# print(bisect.bisect_left(a, [4,1]))
# print(a)


def bisect_left(nums, x):
    l, r = 0, len(nums)
    while l<r:
        m = (l+r)//2
        if nums[m] < x:
            l = m+1
        else:
            r = m
    return l

def bisect_right(nums, x):
    l,r = 0,len(nums)
    while l<r:
        m = (l+r)//2
        if nums[m] <= x:
            l = m+1
        else:
            r=m
    return l



# index = bisect_left(a, 4)

index = bisect_left(a, 6)
# a.insert(index, 6)
print(index, a)