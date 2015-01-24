class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    
    def subsets(self, S):
        # The problem requires non-descending order,
        # but given S might not sorted
        S.sort()
        bset = 1 << len(S)
        ans = []
        for i in range(bset-1, -1, -1):
            cur = []
            for j in range(0, len(S)):
                if (1 << j) & i:
                    cur.append(S[j])
            ans.append(cur)
        return ans

    # Someone's embeded function
    def subsets2(self, S):
        S.sort()
        res = []
        # The benefit of closure
        def dfs(dep, start, buf):
            res.append(buf)
            if dep == len(S):
                return
            for i in range(start, len(S)):
                dfs(dep+1, i+1, buf+[S[i]])
        
        dfs(0, 0, [])
        return res

    # Someone's List comprehension 
    def subsets3(self, S):
        res = [[]]
        for e in sorted(S):
            res = res + [l + [e] for l in res]
        return res
    
        
        
        
if __name__ == '__main__':
    so = Solution()
    ll = [1,2,2]
    print so.subsets3(ll)