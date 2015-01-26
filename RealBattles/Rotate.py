def clockwise(mat):
    n = len(mat)
    for i in xrange(n):
        for j in xrange(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for l in mat:
        l.reverse()
    return mat

def anticlockwise(mat):
    n = len(mat)

    for i in xrange(n):
        for j in xrange(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # column reverse
    for i in xrange(n):
        for j in xrange(n/2):
            mat[j][i], mat[n-j-1][i] = mat[n-j-1][i], mat[j][i]
    return mat

if __name__ == '__main__':
    mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    clock = anticlockwise(mat)
    for i in clock:
        print i
