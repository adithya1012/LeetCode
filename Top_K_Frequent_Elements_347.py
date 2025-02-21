import heapq

# def topKFrequent(nums, k):
#     ele = set()
#     heap = []
#     nums.sort()
#     ele.add(nums[0])
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] not in ele:
#             ele.add(nums[i])
#             heapq.heappush(heap, (-count, nums[i - 1]))
#             count = 0
#         count += 1
#     heapq.heappush(heap, (count, nums[-1]))
#
#     ans = []
#     print(heap)
#     for i in range(k):
#         count, ele = heapq.heappop(heap)
#         print(count, ele)
#         ans.append(ele)
#     return ans

'''
Following is the bucket Sort
'''


def topKFrequent(nums, k):
    counts = {}
    ele_val = [[] for _ in range(len(nums) + 1)]

    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for key, val in counts.items():
        ele_val[val].append(key)
    ans = []
    for i in range(len(ele_val) - 1, 0, -1):
        if ele_val[i]:
            for j in ele_val[i]:
                if k:
                    k -= 1
                    ans.append(j)
                else:
                    break
    return ans


print(topKFrequent([1,1,1,2,2,3], 2))