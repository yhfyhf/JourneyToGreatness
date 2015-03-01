class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        res = -float('inf')
        cur = 0
        for i in A:
            cur = max(cur+i, i)
            res = max(cur, res)
        return res
