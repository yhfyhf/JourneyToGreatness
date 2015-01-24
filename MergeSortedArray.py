class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        # Merge from back to head
        pA = m - 1
        pB = n - 1 
        pM = m + n -1
        while pA >= 0 and pB >= 0:
            if A[pA] > B[pB]:
                A[pM] = A[pA]
                pA -= 1
            else:
                A[pM] = B[pB]
                pB -= 1
            pM -= 1
        while pB >= 0:
            A[pM] = B[pB]
            pB -= 1
            pM -= 1


if __name__ == '__main__':
    so = Solution()
    A = [1,2,3,4,5,8,14,45,0,0,0,0]
    B = [3,7,12,15]
    so.merge(A, 8, B, 4)
                