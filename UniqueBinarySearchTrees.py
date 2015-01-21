class Solution:
    # @return an integer
    def numTrees(self, n):
        d = [0 for x in xrange(n+1)]
        d[0] = d[1] = 1
        for i in xrange(2, n+1):
            for j in xrange(i):
                d[i] += d[j] * d[i-j-1] # left: j, right: i-j-1, root: 1, sum up as i
        return d[n]       

if __name__ == '__main__':
    so = Solution()
    print so.numTrees(3)