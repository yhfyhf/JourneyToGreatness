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

    
if __name__ == '__main__':
    mat = [
        '0000',
        '0010',
        '0110',
        '1011'
    ]
    so = Solution()
    print so.maximalRectangle(mat)