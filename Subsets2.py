class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        res = set()
        def dfs(dep, start, buf):
            res.add(tuple(buf))
            if dep == len(S):
                return
            for i in xrange(start, len(S)):
                dfs(dep+1, i+1, buf+[S[i]])
        dfs(0, 0, [])
        for i in xrange(len(res)):
            res[i] = list(res[i])
        return res

if __name__ == '__main__':
    so = Solution()
    S = [-1,2,2]
    print so.subsetsWithDup(S)
    
    