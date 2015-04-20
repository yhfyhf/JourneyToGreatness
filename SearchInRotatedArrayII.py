class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        l, r = 0, len(A) - 1
        while l <= r:
            mid = l + (r-l)/2
            if A[mid] == target:
                return True
            if A[l] < A[mid]:
                if A[l] <= target and target < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif A[l] > A[mid]:
                if A[mid] < target and target <= A[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # A[l] == A[mid]
                l += 1
        return False

if __name__ == '__main__':
    so = Solution()
    print so.search([4,5,5,6,6,7,7,8,9,9,1,3], 2)
        
