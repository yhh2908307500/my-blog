class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        if m == 0:
            return
        r = []
        c = []
        n = len(matrix[0])
        # 记录需要置零的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        # 需要置零的行
        r = set(r)
        # 需要置零的列
        c = set(c)
        for i in r:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in c:
                matrix[i][j] = 0
