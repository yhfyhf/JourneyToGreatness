import unittest
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def dfs(candidates,idx, target, buff):
            if target == 0 and buff not in res:
                res.append(buff)
                return
            for i in xrange(idx, len(candidates)):
                if target - candidates[i] >= 0:
                    dfs(candidates, i+1, target-candidates[i], buff+[candidates[i]])
        dfs(candidates, 0, target, [])
        return res

if __name__ == '__main__':
    so = Solution()
    print so.combinationSum2([10,1,2,7,6,1,5], 8)