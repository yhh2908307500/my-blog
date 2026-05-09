class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 使用集合检查重复
        return len(nums) != len(set(nums))

    # def containsDuplicate(self, nums):
    #     # 先排序再检查相邻元素
    #     nums.sort()
    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i + 1]:
    #             return True
    #     return False