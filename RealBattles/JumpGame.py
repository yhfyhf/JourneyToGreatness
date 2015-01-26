"""
http://www.geeksforgeeks.org/google-mountain-view-interview/

Find minimum number of steps to reach the end of array from start (array value shows how much you can move)

Jump GameII
[2,3,1,1,4]
"""

def jump(A):
    if not A:
        return 0
    dp = [float('inf') for x in xrange(len(A))]
    dp[0] = 0
    for i in xrange(1, len(A)):
        for j in xrange(i):
            if A[j] >= i-j: # reachable
                dp[i] = min(dp[i], dp[j]+1)
    return dp[len(A)-1]
    