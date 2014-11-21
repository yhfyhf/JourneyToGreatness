'''
http://blog.csdn.net/daniel_ustc/article/details/25692671

dp[i]: The longest increasing subsequence ended in i
initialize: dp[i] = 1

dp[i] = max{1, dp[j]+1 | j<i and A[j]<A[i]}
'''

def lis(A):
    "O(n^2)"
    n = len(A)
    if n < 1:
        return -1

    dp = [1 for x in xrange(n)]
    res = 0
    for i in xrange(n):
        for j in xrange(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j]+1)
                print i, j
                print "dp", dp
                print "\n"
        res = max(res, dp[i])
        
    return res
    


if __name__ == '__main__':
    A = [7,1,6,5,3,4,8]
    print lis(A)