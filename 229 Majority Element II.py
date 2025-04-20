from collections import defaultdict
def majorityElement(nums):
    count = defaultdict(int)
    # print(count[0])
    for i in nums:
        count[i] += 1
        if not len(count) > 2:
            continue
        tmp = defaultdict(int)
        for key, c in count.items():
            if c > 1:
                tmp[key] = c - 1
        count = tmp
    # print(count)
    res = []

    for c in count:
        count_key = 0
        for i in nums:
            if i == c:
                count_key += 1
                if count_key > len(nums) // 3:
                    res.append(c)
                    break
    return res

majorityElement([1,2,3,4])
