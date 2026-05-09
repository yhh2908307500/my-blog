class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if nums is None or len(nums) == 0:
    #         return 0
    #     ls = len(nums)
    #     dp = [0] * ls
    #     # 从0到ls-2的动态规划（不偷最后一个）
    #     dp[0] = nums[0]
    #     for i in range(1, ls - 1):
    #         if i < 2:
    #             dp[i] = max(nums[i], dp[i - 1])
    #         else:
    #             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    #     res = dp[ls - 2]
    #     # 从1到ls-1的动态规划（不偷第一个）
    #     dp[0] = 0
    #     for i in range(1, ls):
    #         if i < 2:
    #             dp[i] = max(nums[i], dp[i - 1])
    #         else:
    #             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    #     return max(res, dp[ls - 1])

    def rob(self, nums):
        # 环形房屋：两种情况取最大值 - 不偷第一个或不偷最后一个
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums, 0, len(nums) - 2),
                   self.rob_helper(nums, 1, len(nums) - 1))


    def rob_helper(self, nums, low, high):
        # 线性房屋打家劫舍
        prevMax = currMax = 0
        for index in range(low, high + 1):
            temp = currMax
            currMax = max(prevMax + nums[index], currMax)
            prevMax = temp
        return currMax
