
def merge(intervals):

    i = 1
    intervals.sort()
    res = [intervals[0]]
    while i < len(intervals):
        if res[-1][1] < intervals[i][0]:

            res.append(intervals[i])
            i += 1
        else:
            if res[-1][1] >= intervals[i][1]:
                i += 1
                continue

            res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            i += 1
    return res

print(merge([[1,4],[0,4]]))