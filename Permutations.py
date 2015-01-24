class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        res = []
        if num == None:
            return res
        def dfs(num, buf):
            if not num:
                res.append(buf)
                return
            for i in xrange(len(num)):
                dfs(num[:i]+num[i+1:], buf+[num[i]])
        dfs(num, [])
        return res

if __name__ == '__main__':
    so = Solution()
    print so.permute([1,2,3])
            