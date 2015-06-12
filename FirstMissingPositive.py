class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        """
        bucket sort, make A[0] = 1, A[1] = 2, A[2] = 3 and so forth
        we only sort need postive integers, which are in [1,n]
        """
        if not A:
            return 1
        n = len(A)
        for i in xrange(n):
            while A[i] != i+1:
                if A[i] <= 0 or A[i] > n or A[i] == A[A[i]-1]:
                    break
                cur = A[i]
                A[i] = A[cur-1]
                A[cur-1] = cur
        for i in xrange(n):
            if A[i]!= i+1:
                return i+1
        return n+1

    def firstMissingPositive2(self, A):
        # Time O(N), Space O(N)
        mx = 0
        poset = set()
        for i in A:
            if i > 0:
                mx = max(mx, i)
                poset.add(i)
        for i in xrange(1, mx):
            if i not in poset:
                return i
        return mx+1
    

if __name__ == '__main__':
    S = [[-1], [2], [1,3,4], [2,0,-4,1,5]]

    so = Solution()
    for k in S:
        print so.firstMissingPositive(k)
