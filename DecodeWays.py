class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [1,1]
        for i in xrange(2, len(s)+1):
            if 10 < int(s[i-2:i]) <= 26 and s[i-1] != '0':
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp.append(dp[i-2])
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]

if __name__ == '__main__':
    so = Solution()
    print so.numDecodings('11')