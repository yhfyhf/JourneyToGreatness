class Solution:
    # @return a list of integers
    def grayCode(self, n):
        # http://www.cnblogs.com/lihaozy/archive/2012/12/31/2840437.html
        res = []
        size = 1 << n
        for i in xrange(size):
            res.append((i>>1)^i)
        return res

if __name__ == '__main__':
    so = Solution()
    print so.grayCode(2)