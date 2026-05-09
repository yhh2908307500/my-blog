class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 自底向上动态规划，时间复杂度O(m*n)
        # https://leetcode.com/discuss/93024/easy-dp-java-solution-with-detailed-explanation
        # 特殊情况：两个字符串完全相等
        if s == p:
            return True
        m, n = len(s), len(p)
        # dp[i][j]表示s的前i个字符和p的前j个字符是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # 处理p以*开头的情况，可以匹配空字符串
        for j in range(1, n):
            if p[j] == '*' and dp[0][j - 1]:
                dp[0][j + 1] = True
        # print dp
        for i in range(m):
            for j in range(n):
                # 字符匹配或.通配
                if p[j] == '.' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                # 处理*通配符
                elif p[j] == '*':
                    # *前面的字符不匹配，只能取0次
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        # 三种情况：取0次、取1次、取多次
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.isMatch("", ".*")


