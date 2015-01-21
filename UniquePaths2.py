class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles0(self, obstacleGrid):
        if len(obstacleGrid) == 0:
            return 0


        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # The necessary initialization is d[0][0..n] and d[0..m][n] to 1
        d = [[1 for x in xrange(n)] for x in xrange(m)]
        
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 1:
                    d[i][j] = 0
                else:
                    tmp = 0
                    if i > 0:
                        tmp += d[i-1][j]
                        if j > 0:
                            tmp += d[i][j-1]
                            if i+j != 0:
                                d[i][j] = tmp

        return d[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        # Scrolling array
        if len(obstacleGrid) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        d = [0 for x in xrange(n)]
        d[0] = 0 if obstacleGrid[0][0] == 1 else 1
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 1:
                    d[j] = 0
                else:
                    if j == 0:
                        d[j] = d[j] # readability
                    else:
                        d[j] = d[j] + d[j-1]

        return d[n-1]
                    


if __name__ == '__main__':
    mat = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    so = Solution()
    print so.uniquePathsWithObstacles(mat)