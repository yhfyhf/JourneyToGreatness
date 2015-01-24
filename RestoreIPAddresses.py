class Solution:
    # @param s, a string
    # @return a list of string
    def restoreIpAddresses(self, s):
        # @param ip: a string
        # @param buf: a list of strings represent ip like ['255', '255', '11', 35']
        def dfs(ip, buf, res):
            if len(ip) > 3*(4-len(buf)):
                return
            if len(buf) == 4:
                if len(ip) == 0:
                    res.append(".".join(buf))
                return
            for i in xrange(1,3+1):
                if ip[:i] and int(ip[:i]) <= 255 and len(ip)>=i:
                    #print 'ip[:i]',ip[:i]
                    if len(ip[:i]) > 1 and ip[:i][0] == '0':
                        break
                    dfs(ip[i:], buf+[ip[:i]], res)
        res = []
        dfs(s, [], res)
        return res


if __name__ == '__main__':
    so = Solution()
    s = "25525511135"
    ss = "1111111111"
    lt = ["25525511135", "1111111111", '010010', '00000']
    for k in lt:
        print so.restoreIpAddresses(k)
        print so.restoreIpAddresses2(k)
        print '\n'

    
