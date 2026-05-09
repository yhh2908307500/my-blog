class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 使用DFS标记岛屿
        if grid is None or len(grid) == 0:
            return 0
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.explore(grid, i, j)
                    islands += 1
        return islands

    def explore(self, grid, i, j):
        # 标记当前位置为已访问
        grid[i][j] = 'X'
        # 向上探索
        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self.explore(grid, i - 1, j)
        # 向左探索
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.explore(grid, i, j - 1)
        # 向下探索
        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.explore(grid, i + 1, j)
        # 向右探索
        if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
            self.explore(grid, i, j + 1)