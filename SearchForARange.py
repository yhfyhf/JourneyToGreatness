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

    def searchRange2(self, A, target):
        def low(A, target):
            p = lambda x: x >= target
            l, r = 0, len(A) - 1
            res = -1
            while l <= r:
                mid = l + (r - l) / 2
                if p(A[mid]):
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1
            res = res if A[res] == target else -1
            return res
            
        def high(A, target):
            p = lambda x: x <= target
            l, r = 0, len(A) - 1
            res = -1
            while l <= r:
                mid = l + (r - l) / 2
                if p(A[mid]):
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            res = res if A[res] == target else -1
            return res
        
        return [low(A, target), high(A, target)]
                
        

if __name__ == '__main__':
    so = Solution()
    print so.searchRange([1,2,2,3,4,5,5,5,5,6], 5)
