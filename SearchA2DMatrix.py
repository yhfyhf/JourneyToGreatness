class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        """
        stupid and ugly
        """
        if not matrix:
            return False
        l, r = 0, len(matrix)
        while l < r:
            mid = l + (r-l)/2
            if matrix[mid][-1] >= target:
                r = mid
            else:
                l = mid + 1
        # important
        if r > len(matrix)-1:
            return False
        ll, rr = 0, len(matrix[0])
        while ll <= rr:
            mid = ll + (rr - ll) / 2
            if matrix[r][mid] > target:
                rr = mid - 1
            elif matrix[r][mid] < target:
                ll = mid + 1
            else:
                return True
        return False



if __name__ == '__main__':
    ma = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    k = [[1]]
    so = Solution()
    so.searchMatrix(k, 2)