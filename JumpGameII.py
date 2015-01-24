
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        """
        @ last: keep track of the maximum distance has been reached
         with the minimum steps so far ("res"), "cur" is the maximum
        distance can be reached by "res+1" steps, when i in [0, last]
        """
        res, last, cur = 0, 0, 0
        for i in xrange(len(A)):
            if i > last:
                last = cur
                res += 1
            cur = max(cur, i+A[i])
        return res
    
    def jump_dp(self, A):
        """
        DP will TLE
        """
        if not A:
            return 0
        dp = [0xffffffff for x in xrange(len(A))]
        dp[0] = 0
        for i in xrange(1, len(A)):
            for j in xrange(i):
                if A[j] >= (i-j):
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[len(A)-1]

if __name__ == '__main__':
    so = Solution()
    print so.jump([2,3,1,1,4])
        