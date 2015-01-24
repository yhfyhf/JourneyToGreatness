class Solution:
    # @param height, a list of integer
    # @return an integer
    # TODO http://blog.csdn.net/abcbc/article/details/8943485
    def largestRectangleArea(self, height):
        stack, best = [], 0
        height.append(-0xffff)
        for k in xrange(len(height)):
            if stack and height[stack[-1]] > height[k]:
                while stack and height[stack[-1]] > height[k]:
                    i = stack.pop()
                    if stack:
                        best = max(best, (k-stack[-1] - 1) * height[i])
                    else:
                        best = max(best, k * height[i])
            stack.append(k)
        return best
            
        
        
if __name__ == '__main__':
    so = Solution()
    t1 = [2,1,5,6,2,3]
    print so.largestRectangleArea([1,2,2])