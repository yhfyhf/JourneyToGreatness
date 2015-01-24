class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        """
        overlapped array
        """
        res = [[1 for x in xrange(rowIndex+1)] for y in range(2)]
        for i in xrange(1, rowIndex+1):
            for j in xrange(1, i):
                res[i%2][j] = res[(i-1)%2][j-1]+res[(i-1)%2][j]
        return res[rowIndex%2]

if __name__ == '__main__':
    so = Solution()
    print so.getRow(1)