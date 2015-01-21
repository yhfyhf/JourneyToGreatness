'''
   ---> word2
  |
  | 
word1

    None   a   b   c
None   0   1   2   3
   a   1   0   1   2
   b   2   1   0   1
   e   3   2   1   1
'''

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if word1 and not word2:
            return len(word1)
        if not word1 and word2:
            return len(word2)

        # initialize
        dp = [[0 for x in xrange(len(word2)+1)] for x in xrange(len(word1)+1)]
        for i in xrange(len(dp[0])):
            dp[0][i] = i
        for j in xrange(len(dp)):
            dp[j][0] = j

        for i in xrange(1, len(dp)):
            for j in xrange(1, len(dp[0])):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))


        return dp[len(dp)-1][len(dp[0])-1]

    # Use overlapped arrary
    def minDistance2(self, word1, word2):
        if word1 and not word2:
            return len(word1)
        if not word1 and word2:
            return len(word2)
        # Initialize
        dp = [[0 for x in xrange(len(word2)+1)] for x in xrange(2)]
        for i in xrange(len(dp[0])):
            dp[0][i] = i
        
        for i in xrange(1, len(word1)+1):
            dp[i&1][0] = i
            for j in xrange(1, len(word2)+1):
                dp[i&1][j] = min(dp[(i-1)&1][j]+1, dp[i&1][j-1]+1, dp[(i-1)&1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))

                
        return dp[len(word1)&1][len(word2)]
            
            
        


if __name__ == '__main__':
    so = Solution()
    w1 = 'abasfasc'
    w2 = 'abasae'
    print so.minDistance(w1,w2)
    print so.minDistance2(w1, w2)
