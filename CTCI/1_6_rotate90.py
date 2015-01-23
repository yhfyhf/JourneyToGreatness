# Leetcode: Rotate Image
def rotate(arr):
    n = len(arr)
    for i in xrange(n):
        for j in xrange(i+1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in xrange(n):
        arr[i].reverse()
    return arr
        
if __name__ == '__main__':
    arr = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    res = rotate(arr)
    for l in res:
        print l