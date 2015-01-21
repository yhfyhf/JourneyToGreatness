class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dic):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i] is False:
                continue
            for j in dic:
                if j == s[i:i+len(j)]:
                    dp[i+len(j)] = True
                continue
                    
        
        return dp[len(s)]

so = Solution()
print so.wordBreak("leetcode",['leet', 'code'])