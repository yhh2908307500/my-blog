class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心算法：从后往前找能到达终点的位置
        # https://leetcode.com/articles/jump-game/
        length = len(nums)
        begin = length - 1
        for i in reversed(range(length - 1)):
            if i + nums[i] >= begin:
                begin = i
        return not begin