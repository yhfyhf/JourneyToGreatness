class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        """
        use two pointers to keep left and right barrier, scan twice(both directions)
        """
        if not A:
            return 0
        n = len(A)
        FA = A[:]
        l, r = 0, 0
        for i in xrange(n):
            if FA[i] >= FA[l]:
                r = i
                for j in xrange(l, r):
                    FA[j] = FA[l]
                l = i

        l, r = n-1, n-1
        for i in xrange(n-1, -1, -1):
            if FA[i] >= FA[r]:
                l = i
                for j in xrange(l+1, r+1):
                    FA[j] = FA[r]
                r = i
        return sum(FA)-sum(A)

if __name__ == '__main__':
    so = Solution()
    print so.trap([0,1,0,2,1,0,1,3,2,1,2,1])