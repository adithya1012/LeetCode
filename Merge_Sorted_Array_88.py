class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0

        def swap(i, j):
            tmp = nums1[i]
            nums1[i] = nums2[j]
            nums2[j] = tmp
        if not nums2:
            return
        while i<len(nums1):
            if i == len(nums1)-len(nums2):
                for ii in nums2:
                    nums1[i] = ii
                    i+=1
                break
            if nums1[i]>nums2[j]:
                swap(i, j)
                i+=1
                nums2.sort()
            else:
                i+=1