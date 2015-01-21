class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        if n <= 0 or k<= 0:
            return res
        def dfs(start, buf):
            if len(buf) == k:
                res.append(buf)
                return
            for i in xrange(start,n+1):
                dfs(i+1, buf+[i])

        dfs(1, [])
        return res
if __name__ == '__main__':
    so = Solution()
    print so.combine(4, 2)
                