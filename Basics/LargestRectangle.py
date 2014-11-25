
def largestRec(matrix):
    if not matrix:
        return 0
    h,w = len(matrix), len(matrix[0])
    H = [0 for x in range(w)] 
    L = [0 for x in range(w)]
    R = [w for x in range(w)]
    ret = 0
    
    for i in range(h):
        left, right = 0, w
        for j in range(w):
            if matrix[i][j] == 1:
                H[j] += 1
                L[j] = max(L[j], left)
            else:
                left = j + 1
                H[j], L[j], R[j] = 0, 0, w
        # caculate R[i,j] from right to left
        for j in range(w-1, -1, -1):
            if matrix[i][j] == 1:
                R[j] = min(R[j], right)
                ret = max(ret, H[j] * (R[j] - L[j]))
            else:
                right = j
    return ret

if __name__ == '__main__':
    mat = [ [0,0,1,0,0],
            [0,1,1,1,0],
            [0,1,1,1,0],
            [0,1,0,1,1]]
    print largestRec(mat)