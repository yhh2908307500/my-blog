class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划：两种情况
        ls = len(s)
        if ls == 0:
            return 0
        dp = [0] * ls
        for index in range(ls):
            # 情况1：两位数解码（10-26）
            if index >= 1 and int(s[index - 1:index + 1]) < 27 and int(s[index - 1:index + 1]) >= 10:
                if index == 1:
                    dp[index] = 1
                else:
                    dp[index] += dp[index - 2]
            # 情况2：一位数解码（1-9）
            if int(s[index]) != 0:
                if index == 0:
                    dp[index] = 1
                else:
                    dp[index] += dp[index - 1]
        return dp[ls - 1]
