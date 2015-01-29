class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return None
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for x in xrange(n)] for y in xrange(m)]
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        for i in xrange(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        for j in xrange(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])

        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]
        
if __name__ == '__main__':
    mat = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    m = [[0,-3]]
    so = Solution()
    print so.calculateMinimumHP(m)