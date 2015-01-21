class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        dp = [[0 for x in xrange(len(T)+1)] for y in xrange(len(S)+1)]
        for i in xrange(len(S)+1):
            dp[i][0] = 1
        for i in xrange(1, len(S)+1):
            for j in xrange(1, len(T)+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(S)][len(T)]

if __name__ == '__main__':
    so = Solution()
    print so.numDistinct("rabbbit", "rabbit")