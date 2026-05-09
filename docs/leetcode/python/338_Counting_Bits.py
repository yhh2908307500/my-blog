class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            # 动态规划：去掉最后一位 + 最后一位
            res[i] = res[i >> 1] + (i & 1)
        return res

