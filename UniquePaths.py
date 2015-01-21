class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        # Use rolling array(Am i translate it right)
        if m*n == 1:
            return 1
            
        #d = [[1 for x in xrange(n)] for x in xrange(m)]
        t = [1 for x in xrange(n)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                #d[i][j] = d[i-1][j] + d[i][j-1]
                t[j] += t[j-1]
                    
        return t[n-1]#d[m-1][n-1]