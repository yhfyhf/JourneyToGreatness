class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2 
            if A[mid] == target:
                return mid
            elif target > A[mid]:
                left = mid + 1
            else:
                right = mid - 1
    
        return left

if __name__ == '__main__':
    so = Solution()
    Ak = [1,3,4,6,7,8]
    A = [1]
    k = 5
    print so.searchInsert(A, k)