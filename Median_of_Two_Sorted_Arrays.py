class Solution:

    # Space O(1), Time O(lg(m+n))
    # http://yucoding.blogspot.com/2013/01/leetcode-question-50-median-of-two.html
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self._getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return  ( self._getKth(A, B, (lenA + lenB)/2) +
                self._getKth(A, B, (lenA + lenB)/2 + 1) ) / 2.0

    def _getKth(self, A, B, k):
        lenA, lenB = len(A), len(B)
        # ensure A is the shorter one
        if lenA > lenB:
            return self._getKth(B, A, k)
        # A is empty, get from B (-1 for 0 based index)
        if lenA == 0:
            return B[k-1]
        # Edge case
        if k == 1:
            return min(A[0], B[0])

        pa = min(k/2, lenA)
        pb = k - pa
        if A[pa-1] <= B[pb-1]:
            return self._getKth(A[pa:], B, k-pa)
        else:
            return self._getKth(A, B[pb:], k-pb)



        

        
if __name__ == '__main__':
    so = Solution()
    #print so.findMedianSortedArrays([1,2,5,6],[3,3])
    A = [1,3,5,7]
    B = [2,4,6,8,9,10]
    print so.findMedianSortedArrays(B,A)
   