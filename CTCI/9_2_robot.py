def ways(obstacleGrid):
    if not obstacleGrid:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for x in xrange(n)] for y in xrange(m)]
    for i in xrange(m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = 1
        else:
            break
    for i in xrange(n):
        if obstacleGrid[0][i] == 0:
            dp[0][i] = 1
        else:
            break

    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = 0 if obstacleGrid[i][j] == 1 else dp[i-1][j] + dp[i][j-1]
            
    return dp[m-1][n-1]