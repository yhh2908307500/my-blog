class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # 方法1：动态规划，使用dp数组
    #     ls = len(nums)
    #     if ls == 0:
    #         return 0
    #     dp = [0] * ls
    #     dp[0] = nums[0]
    #     for i in range(1, ls):
    #         if i < 2:
    #             dp[i] = max(nums[i], dp[i - 1])
    #         else:
    #             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    #     return dp[ls - 1]

    # def rob(self, nums):
    #     # 方法2：动态规划，原地修改数组
    #     if nums is None or len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
    #     nums[1] = max(nums[0], nums[1])
    #     for i in range(2, len(nums)):
    #         nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
    #     return nums[-1]

    def rob(self, nums):
        # 方法3：动态规划，空间优化为O(1)
        prevMax = currMax = 0
        for num in nums:
            temp = currMax
            currMax = max(prevMax + num, currMax)
            prevMax = temp
        return currMax
