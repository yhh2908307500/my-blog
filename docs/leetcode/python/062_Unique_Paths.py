class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 动态规划：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dmap = [[0] * n for _ in range(m)]
        # 第一行和第一列初始化为1
        for i in range(m):
            dmap[i][0] = 1
        for j in range(n):
            dmap[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                l = u = 0
                if i-1 >= 0:
                    u = dmap[i-1][j]
                if j-1>= 0:
                    l = dmap[i][j-1]
                dmap[i][j] = l + u
        return dmap[m-1][n-1]
