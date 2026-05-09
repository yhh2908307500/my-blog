class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 二分查找
        # 如果start < mid，左半部分有序
        # 如果mid < end，右半部分有序
        def get(start, end):
          if start > end:
            return -1
          mid = (start + end) / 2
          if nums[mid] == target:
            return mid
          elif nums[mid] >= nums[start]: # 左半部分有序
            if target >= nums[start] and target < nums[mid]:
              return get(start, mid - 1)
            else:
              return get(mid + 1, end)
          elif nums[mid] <= nums[end]: # 右半部分有序
            if target > nums[mid] and target <= nums[end]:
              return get(mid + 1, end)
            else:
              return get(start, mid - 1)
        return get(0, len(nums) - 1)