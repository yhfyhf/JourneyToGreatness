class Solution:
    # @param s, a string
    # @return a list of lists of string
    def isPalindrom(self, s):
        for i in xrange(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
        
    def partition(self, s):
        res = []
        def dfs(s, buf):
            if len(s) == 0:
                res.append(buf)
                return
            for i in xrange(1, len(s)+1):
                if self.isPalindrom(s[:i]):
                    dfs(s[i:], buf+[s[:i]])
        dfs(s, [])
        return res
        