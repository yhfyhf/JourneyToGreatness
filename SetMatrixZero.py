class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix:
            return
        cols = [False for x in xrange(len(matrix))]
        rows = [False for x in xrange(len(matrix[0]))]

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols[i], rows[j] = True, True
        for i n xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if cols[i] or rows[j]:
                    matrix[i][j] = 0

        



if __name__ == '__main__':
    ret = [[3,4,1,2,3,4,5,7],[3,4,1,2,3,0,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[0,4,1,2,3,4,5,7],[3,4,9,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,0],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,7],[3,4,1,2,3,4,5,5]]
    so = Solution()
    so.setZeroes(ret)
    for l in ret:
        print '  '.join(str(i) for i in l)
    