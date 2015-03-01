class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        # Time O(N), Space O(1)
        r, w, b = 0, 0, len(A) - 1
        while w <= b:
            if A[w] == 0:
                A[w], A[r] = A[r], A[w]
                r += 1
                w += 1
            elif A[w] == 2:
                A[w], A[b] = A[b], A[w]
                b -= 1
            else:
                w += 1

if __name__ == '__main__':
    A = [1, 0]
    so = Solution()
    so.sortColors(A)
    print A
