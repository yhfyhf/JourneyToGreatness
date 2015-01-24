class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        def rotate_layer(start, end):
            if start >= end:
                return
            for i in xrange(end-start):
                tmp = matrix[start][start+i]
                matrix[start][start+i] = matrix[end-i][start]
                matrix[end-i][start] = matrix[end][end-i]
                matrix[end][end-i] = matrix[start+i][end]
                matrix[start+i][end] = tmp
            rotate_layer(start+1, end-1)
            
        rotate_layer(0, len(matrix)-1)
        return matrix

    # http://www.cnblogs.com/zuoyuan/p/3772978.html
    def rotate2(self, matrix):
        n = len(matrix)
        # diagonal flip
        for i in xrange(n):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(n):
            matrix[i].reverse()
        return matrix

        
            

if __name__ == '__main__':
    matrix = [[0,1,2],[3,4,5],[6,7,8]]
    m =[]
    so = Solution()
    res = so.rotate2(matrix)
    for l in res:
        print l