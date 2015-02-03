"""
1, 2 or 3 steps at a time, possible way to get n
"""

def count_ways(n):
    if n == 0:
        return 0
    dp = [1 for x in xrange(n+1)]
    if n <= 3:
        return 1<<(n-1)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in xrange(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]


if __name__ == '__main__':
    count_ways(10)

    
    