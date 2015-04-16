class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    # TODO 
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        a = [0 for i in xrange(len(matrix[0]))]
        maxArea = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                a[j] = a[j] + 1 if matrix[i][j] == '1' else 0
            # print a
            maxArea = max(maxArea, self.largestRectangleArea(a))
        return maxArea
        
    def largestRectangleArea(self, height):
        stack = []
        i, area = 0, 0
        while i < len(height):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if not stack else i-stack[-1]-1
                area = max(area, width*height[curr])
                i -= 1
            i += 1
        while stack:
            curr = stack.pop()
            width = i if not stack else len(height) - stack[-1]-1
            area = max(area, width*height[curr])
        return area
    
    def maximalRectangle3(self, matrix):
        """
        https://leetcode.com/discuss/20240/share-my-dp-solution
        left(i, j) to enumerate the left edge
        left(i, j) = max(left(i-1, j) curleft)

        right(i, j) to enumerate the right edge(right+1, actually)
        right(i, j) = min(right(i-1, j), curright)

        height(i, j) to enumerate high-down continues '1' cells
        height(i, j) = height(i-1, j) + 1 if matrix[i][j] == '1'
        else height(i, j) = 0
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [0 for x in xrange(n)]
        right = [n for x in xrange(n)]
        height = [0 for x in xrange(n)]

        res = 0
        for i in xrange(m):
            cur_left, cur_right = 0, n
            for j in xrange(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                    
            for j in xrange(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    # initial to 0, for next row usage, not mean current left is 0
                    # because we know for sure this cell's height is 0
                    left[j] = 0 
                    cur_left = j + 1

            for j in xrange(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
                    
            for j in xrange(n):
                res = max(res, (right[j] - left[j]) * height[j])
                
        return res
                        
                

    
if __name__ == '__main__':
    mat = [
        '0000',
        '0010',
        '0110',
        '1011'
    ]
    m = [
        '01110',
        '11001',
        '11110',
        '11110'
    ]
    so = Solution()
    #print so.maximalRectangle(mat)
    print so.maximalRectangle3(m)
