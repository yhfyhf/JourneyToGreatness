class Solution:
    # @param s, a string
    # @return an integer
    # http://fisherlei.blogspot.com/2013/03/leetcode-palindrome-partitioning-ii.html
    def minCut(self, s):
        """
        @dp: how many palindromes in the string
        """
        dp = [0 for i in xrange(len(s)+1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]
        # initialize to worst case
        for i in range(len(s)+1):
            dp[i] = len(s) - i

        for i in xrange(len(s)-1, -1, -1):
            for j in xrange(i, len(s)):
                if s[i] == s[j] and (((j-i) < 2) or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        return dp[0]-1

if __name__ == '__main__':
    so = Solution()
    print so.minCut("cabababcbc")
    print so.minCut("ccaacabacb")

