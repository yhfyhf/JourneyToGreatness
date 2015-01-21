
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        wordset = set(dict)
        maxlen = max(map(len, dict))
        res = []
        def dfs(s, buf):
            if not s:
                # not found or found a solution
                res.append(buf)
                return
            llen = min(maxlen, len(s))
            for i in xrange(llen):
                if s[:i+1] in wordset:
                    dfs(s[i+1:], buf+[s[:i+1]])
        dfs(s, [])
        for i in xrange(len(res)):
            res[i] = ' '.join(res[i])
        return res

    def wordBreak2(self, s, dict):
        wordset = set(dict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        res = []
     
        def dfs(start, buf):
            if start == len(s):
                res.append(buf)
                return
            if dp[start]:
                for end in xrange(start, len(s)):
                    if s[start:end+1] in wordset:
                        dp[end+1] = True
                        dfs(end+1, buf+[s[start:end+1]])
        dfs(0, [])
        for i in xrange(len(res)):
            res[i] = ' '.join(res[i])
        return res

    # Other's AC code
    def check(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]
                        
    def dfs(self, s, dict, stringlist):
        if self.check(s, dict):
            if len(s) == 0: Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:], dict, stringlist+' '+s[:i])
                    
    def wordBreak3(self, s, dict):
        Solution.res = []
        self.dfs(s, dict, '')
        return Solution.res

if __name__ == '__main__':
    so = Solution()
    dic = ["cat", "cats", "and", "sand", "dog"]
    s = "catsanddog"
    #s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    #dic = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print so.wordBreak3(s, dic)
    print so.wordBreak2(s, dic)

            
            
            
            
        
            
         