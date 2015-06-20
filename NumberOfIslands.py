class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if len(grid) < 1:
            return 0
        height, width = len(grid), len(grid[0])
        mark = [[False for y in range(width)] for x in range(height)]
        res = 0
        for i in range(height):
            for j in range(width):
                if self.dfs(i, j, grid, mark):
                    res += 1
        return res

    def dfs(self, i, j, grid, mark):
        """
        Args:
            i, j: int value to mark coord
            mark: 2D Boolean matrix to mark visited
        Returns:
            True if this is a new island
        """
        if i < 0 or j < 0 or i >= len(mark) or j >= len(mark[0]):
            return False
        if grid[i][j] == '0' or mark[i][j]:
            return False
        mark[i][j] = True
        self.dfs(i - 1, j, grid, mark)
        self.dfs(i + 1, j, grid, mark)
        self.dfs(i, j - 1, grid, mark)
        self.dfs(i, j + 1, grid, mark)
        return True
