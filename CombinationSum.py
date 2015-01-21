class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # for non-desending order
        candidates.sort()
        res = []
        def dfs(candidates, idx, target, buff):
            if target == 0:
                res.append(buff)
                return
            for i in xrange(idx, len(candidates)):
                if target - candidates[i] >= 0:
                    dfs(candidates, i, target-candidates[i], buff+[candidates[i]])
        dfs(candidates, 0, target, [])
        return res

if __name__ == '__main__':
    so = Solution()
    print so.combinationSum([2,3,6,7], 7)
                    