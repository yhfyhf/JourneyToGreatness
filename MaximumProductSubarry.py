
def maxProduct(A):
    # Brute force, O(n^2)
    if len(A) == 0:
        return 0
    n = len(A)
    tab = [[0 for x in range(n)] for x in range(n)]
    res = 0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                tab[i][j] = A[i]
            else:
                tab[i][j] = tab[i][j-1] * A[j]
            res = max(res, tab[i][j])
    return res

def maxProduct1(A):
    # DP, the minimum value could change to maximum by times a negative
    # while the maximum could change to minimum
    # The key point is to maintain the largest abs value.
    
    if len(A) == 0:
        return 0
    cur_min = A[0]
    cur_max = A[0]
    res = A[0]
    for i in range(1, len(A)):
        a = A[i] * cur_min
        b = A[i] * cur_max
        c = A[i]
        cur_max = max(max(a, b), c)
        cur_min = min(min(a, b), c)
        res = max(res, cur_max)
    return res
    

if __name__ == '__main__':
    A = [1,3,-4,2,-9,-1]
    print largestRec(A)