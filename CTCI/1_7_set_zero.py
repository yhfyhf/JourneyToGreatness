# Leetcode: Set Matrix Zero
def setZero(matrix):
    if not matrix:
        return matrix
    col = [False for x in xrange(len(matrix))]
    row = [False for x in xrange(len(matrix[0]))]
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            if matrix[i][j] == 0:
                col[i], row[j] = True, True
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            if col[i] or row[j]:
                matrix[i][j] = 0
    return matrix

if __name__ == '__main__':
    mat = [
        [1,2,3,4],
        [3,0,1,4],
        [0,0,4,8],
        [8,4,2,6]
    ]
    for l in setZero(mat):
        print l
