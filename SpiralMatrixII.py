class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        res = [[0 for x in xrange(n)] for x in xrange(n)]
        if n == 0:
            return res
        left, right = 0, n - 1
        up, down = 0, n - 1
        cnt = 1
        while True:
            for i in xrange(left, right+1):
                res[up][i] = cnt
                cnt += 1
            up += 1
            for i in xrange(up, down+1):
                res[i][right] = cnt
                cnt += 1
            right -= 1
            for i in xrange(right, left-1, -1):
                res[down][i] = cnt
                cnt += 1
            down -= 1
            for i in xrange(down, up-1, -1):
                res[i][left] = cnt
                cnt += 1
            left += 1
            
            if left > right or up > down:
                break
        return res

if __name__ == '__main__':
    so =Solution()
    print so.generateMatrix(4)
            