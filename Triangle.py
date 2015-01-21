class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
            
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
