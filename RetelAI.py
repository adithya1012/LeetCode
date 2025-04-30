#
#
# def minTime(workers, totalJobs):
#     # Leaner Search
#     # total_job = 0
#     # count = 0
#     # while total_job < totalJobs:
#     #     count += 1
#     #     for i in workers:
#     #         if count%i == 0:
#     #             total_job += 1
#     #
#     # return count
#
#     left = 1
#     right = max(workers)*totalJobs
#
#     while left<right:
#         m = (left+right)//2
#         if sum(m//i for i in workers) < totalJobs:
#             left=left+1
#         else:
#             right=right-1
#     return left
#
#
# print(minTime([5,7,9], 5))

import collections

def countBinarySubstrings(s):
    N = len(s)
    prev, cur = 0, 1
    output = 0
    for i in range(1,N):
        if s[i]!=s[i-1]:
            output+=min(prev, cur)
            prev = cur
            cur = 1
        else:
            cur+=1
    return output+min(prev, cur)


print(countBinarySubstrings("00110011"))


