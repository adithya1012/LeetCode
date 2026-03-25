
# You are given a list of scheduled ad campaigns, each with a (start_time, end_time) in seconds. Return the minimum number of parallel ad slots required to run all campaigns without time overlap.


# Input: [(1, 5), (3, 6), (7, 9)]
# Output: 2
# Explanation: 
# [1,5] and [3,6] overlap → need 2 slots
# [7,9] starts after → reuse

class Solution:
    def __init__(self):
        pass

    def scheduler(self, timings):
        start = sorted([i[0] for i in timings])
        end = sorted([i[1] for i in timings])

        res = 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                s+=1
            else:
                e+=1
            res = max(s - e, res)
        print(res)


Solution().scheduler([(1, 5), (3, 6), (7, 9)])
# Solution().scheduler([(1, 5), (5,6)]) # 1
