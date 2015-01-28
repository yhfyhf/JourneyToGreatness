class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        left, right = 0, len(num)-1
        while left <= right:
            mid = left + (right - left)/2
            if left == right:
                return left
            if num[mid] < num[mid+1]:
                left = mid + 1
            else:
                right = mid

if __name__ == '__main__':
    so = Solution()
    print so.findPeakElement([1,2,4,6,7,10,1])