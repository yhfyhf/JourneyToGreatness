class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        idx = 2
        for i in xrange(2, len(A)):
            if A[i] != A[idx-2]:
                A[idx] = A[i]
                idx += 1
        return idx

if __name__ == '__main__':
    A = [1,2,3,3,3,4,6,7,7]
    so = Solution()
    idx = so.removeDuplicates(A)
    print A[:idx]
    