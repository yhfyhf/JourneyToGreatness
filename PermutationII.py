class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        res = []
        if num == None:
            return res
        num.sort()
        def dfs(num, buf):
            if not num:
                res.append(buf)
                return 
            for i in xrange(len(num)):
                if i >= 1 and num[i] == num[i-1]:
                    continue
                dfs(num[:i]+num[i+1:],buf+[num[i]])
        dfs(num, [])
        return res

if __name__ == '__main__':
    so = Solution()
    ss = "aaab"
    print so.permuteUnique(list(ss))
