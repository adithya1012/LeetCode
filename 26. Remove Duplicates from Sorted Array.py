
def removeDuplicates(nums):
    s = nums
    l, r = 0, len(nums) - 1
    seen = set()
    while l <= r:
        if s[l] in seen:
            tmp = s[l]
            s[r] = s[l]
            s[l] = tmp
            r -= 1
        else:
            seen.add(s[l])
            l += 1
    return len(seen)

print(removeDuplicates([1,1,2]))