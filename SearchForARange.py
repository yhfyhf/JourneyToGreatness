class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        low, high = -1, -1
        if not A:
            return [low, high]
            
        left, right = 0, len(A)-1
        while left <= right:
            mid = left + (right-left)/2
            if A[mid] >= target:
                low = mid
                right = mid - 1
            else:
                left = mid + 1
        low = low if A[low] == target else -1
        left, right = 0, len(A)-1
        while left <= right:
            mid = left + (right-left)/2
            if A[mid] <= target:
                high = mid
                left = mid + 1
            else:
                right = mid - 1
        high = high if A[high] == target else -1
        return [low, high]
        

if __name__ == '__main__':
    so = Solution()
    print so.searchRange([1,2,2,3,4,5,5,5,5,6], 5)