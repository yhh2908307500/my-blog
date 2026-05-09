class Solution(object):
    # def findMin(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     return self.get_min(nums, 0, len(nums) - 1)
    #
    # def get_min(self, nums, start, end):
    #     mid = (start + end) / 2
    #     if start == end:
    #         # one element
    #         return nums[start]
    #     if mid == start or mid == end:
    #         # two element
    #         return min(nums[start], nums[end])
    #     if nums[mid] < nums[end]:
    #         # right side sorted
    #         if nums[mid] > nums[start]:
    #             # not rotated
    #             return nums[start]
    #         return self.get_min(nums, start, mid)
    #     elif nums[mid] > nums[end]:
    #         # left side sorted
    #         return self.get_min(nums, mid, end)

    def findMin(self, nums):
        # 二分查找：如果左半部分有序，最小值在右半部分；反之在左半部分
        l, r = 0, len(nums) - 1
        while l < r and nums[l] >= nums[r]:
            mid = (l + r) / 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

