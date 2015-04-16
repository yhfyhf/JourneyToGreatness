class Solution:
    # @param height, a list of integer
    # @return an integer
    # TODO http://blog.csdn.net/abcbc/article/details/8943485
    def largestRectangleArea_old(self, height):
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

    # http://fisherlei.blogspot.ca/2012/12/leetcode-largest-rectangle-in-histogram.html
    def largestRectangleArea(self, hist):
        s = []
        i, max_area = 0, 0
        while i < len(hist):
            if not s or hist[s[-1]] <= hist[i]:
                s.append(i)
                i += 1
            else:
                idx = s.pop()
                # stack 存递增，hist[i] < s[-1], 此处是个极值，可以展开看 area
                top_area = hist[idx] * (i if not s else i - s[-1] - 1)
                print 'i %d, idx %d, hist[idx] %d, width %d, top_area %d' % (i, idx, hist[idx],  (i if not s else i - s[-1] - 1), top_area)
                print s, '\n'
                max_area = max(max_area, top_area)
        while s:
            idx = s.pop()
            top_area = hist[idx] * (i if not s else i - s[-1] - 1)
            max_area = max(max_area, top_area)        
        return max_area

    # raw O(n^2) method
    def largestRectangleArea(self, height):
        res = 0
        for left in range(len(height)):
            cur_height = height[left]
            for right in range(left+1, len(height)):
                cur_height = min(cur_height, height[right])
                res = max(res, (right - left + 1)* cur_height)
        return res

if __name__ == '__main__':
    so = Solution()
    t1 = [2,1,5,6,2,3]
    print so.largestRectangleArea(t1)
    print so.largestRectangleArea2(t1)
