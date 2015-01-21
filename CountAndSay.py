class Solution:
    def _iteration(self, s):
        cur, cnt = None, 0
        res = ""
        for i in xrange(len(s)):
            if s[i] != cur:
                if cur:
                    res += str(cnt) + cur
                cur = s[i]
                cnt = 1
            else:
                cnt += 1
        res += str(cnt) + cur
        return res
        
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for _ in xrange(2, n+1):
            s = self._iteration(s)
        return s

if __name__ == '__main__':
    so = Solution()
    print so.countAndSay(5)
                
            