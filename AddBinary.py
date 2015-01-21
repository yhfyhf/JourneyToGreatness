class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        # edge check
        a, b = map(int, list(a)), map(int, list(b))
        na, nb = len(a)-1, len(b)-1
        res = []
        while na >= 0 and nb >= 0:
            res.append(a[na]+b[nb])
            na -= 1
            nb -= 1
            
        while na >= 0:
            res.append(a[na])
            na -= 1
        while nb >= 0:
            res.append(b[nb])
            nb -= 1

        carry = 0
        for i in xrange(len(res)):
            res[i] += carry
            if res[i] >= 2:
                res[i] %= 2
                carry = 1
            else:
                carry = 0
        if carry:
            res.append(1)
        return ''.join(map(str, res[::-1]))
                

if __name__ == '__main__':
    so = Solution()
    print so.addBinary('0','1')
                                