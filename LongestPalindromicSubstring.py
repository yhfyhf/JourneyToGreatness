class Solution:
    # @return a string
    # P(i,j) = true if S[i:j+1] is palindrome
    def longestPalindrome(self, s):
        lenS = len(s)
        if lenS == 0:
            return ''
        dp = {}
        for i in range(lenS):
            dp[(i,i)] = True
        # k range from 0 to n-1
        for k in range(lenS-1):
            for i in range(lenS):
                j = i + k
                if j >= lenS: continue
                if i+1 <= j-1:
                    dp[(i,j)] = dp[(i+1,j-1)] and s[i] == s[j] # Good Trick
                else: # i,j is adjacent or i == j
                    dp[(i,j)] = s[i] == s[j]

        # In all palindrome substr, find longest( j-i is max)
        begin, end = max([k for k in dp if dp[k]], key=lambda x:x[1]-x[0])
        return s[begin:end+1]

    # Simple, Time O(n^2), Space O(1)
    def lp(self, s):
        lenS = len(s)
        if lenS == 0:
            return ''
        maxstr = ''
        for i in range(lenS):
            for j in [i,i+1]: # enumerate j as i, i+1
                 # Expand from s[i], s[i+1] (even, odd)
                ci, cj = i,j
                while ci >= 0 and cj<= lenS-1:
                     if s[ci] != s[cj]: # used to judge s[i] ?= s[i+1]
                         break
                     # s[i] == s[j]
                     curstr = s[ci:cj+1]
                     ci -= 1
                     cj += 1
                #curstr = s[i:j+1]
                
                if len(curstr) > len(maxstr):
                    maxstr = curstr
        return maxstr
                    
                

if __name__ == '__main__':
    so = Solution()
    s ="bbbb"
    # print so.longestPalindrome(s)
    print so.lp(s)