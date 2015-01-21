class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows <= 1:
            return s
        res = ""
        interval = 2*nRows-2
        for i in xrange(nRows):
            for j in xrange(i, len(s), interval):
                res += s[j]
                if i != 0 and i != nRows-1 and j + interval - 2*i < len(s):
                    res += s[j+ interval-2*i]
        return res