class Solution:

    # Space O(1), Time O(lg(m+n))
    # http://yucoding.blogspot.com/2013/01/leetcode-question-50-median-of-two.html
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.__getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return  ( self.__getKth(A, B, (lenA + lenB)/2) +
                self.__getKth(A, B, (lenA + lenB)/2 + 1) ) / 2.0

    def __getKth(self, A, B, k):
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

        ath = min(k/2, lenA)
        bth = k - ath
        # depend on ath element of A (A[ath-1]) and bth element of B
        # (B[bth-1]), we can get remove either ath or bth element
        if A[ath-1] <= B[bth-1]:
            return self.__getKth(A[ath:], B, k-ath)
        else:
            return self.__getKth(A, B[bth:], k-bth)


    def getKth(A, B, k):
        # @param A, B: list A and B
        # @param k: kth element, based on 1~k
        print 'k:', k, '\nA:', A, '\nB:', B, '\n'
        lenA, lenB = len(A), len(B)
        # make sure A is shorter one
        if lenA > lenB:
            getKth(B, A, k)
        if lenA == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
     
        ath = min(k / 2, lenA)
        bth = k - ath
     
        # if A[ath - 1] <= B[bth-1]:
        #     return getKth(A[ath:], B, k - ath)
        # else:
        #     return getKth(A, B[bth:], k - bth)
        if A[ath - 1] < B[bth - 1]:
            return getKth(A[ath:], B, k - ath)
        elif A[ath - 1] > B[bth - 1]:
            return getKth(A, B[bth:], k - bth)
        else:
            return A[ath - 1] # or B[bth - 1]

        
if __name__ == '__main__':
    so = Solution()
    # print so.findMedianSortedArrays([1,2,5,6],[3,3])
    A = [1,3,5,7,11]
    B = [2,4,6,8,9,10]
    #print so.__getKth(A, B, 1)
    print so.findMedianSortedArrays(A, B)
   
