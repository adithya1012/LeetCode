class Solution:
    def check(self, nums) -> bool:
        breaks = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                breaks += 1

        if nums[0] < nums[-1]:
            breaks += 1
        print(breaks)
        return breaks <= 1

print(Solution().check([[3,4,5,1,2]]))