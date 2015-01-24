class Solution:
    # http://www.cnblogs.com/zuoyuan/p/3769829.html
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        """
        keep 4 borders
        """
        res= []
        if not matrix:
            return res
        up, left = 0, 0
        down, right = len(matrix)-1, len(matrix[0])-1
        direction = 0 # 0:right 1:down 2:left 3:up
        while True:
            if direction == 0:
                for i in xrange(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            elif direction == 1:
                for i in xrange(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in xrange(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            else: # 3
                for i in xrange(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right:
                return res
            direction = (direction+1) % 4
        return res

if __name__ == '__main__':
    so = Solution()
    mat = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    print so.spiralOrder(mat)