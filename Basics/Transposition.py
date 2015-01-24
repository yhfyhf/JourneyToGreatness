mat = [[1,2],[3,4],[5,6]]

res = [0 for x in xrange(6)]

m, n = len(mat),len(mat[0])
for i in xrange(m):
    for j in xrange(n):
        res[i*n+j] = mat[i][j]

print res