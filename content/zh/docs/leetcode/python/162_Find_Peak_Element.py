# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

class Solution(object):
    def findPeakElement(self, nums):
        # 二分查找：如果mid小于mid+1，峰值在右边；否则在左边
        # note that num[-1] = num[n] = -∞
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] < nums[mid+1]:
                start= mid + 1
            else:
                end = mid
        return start
