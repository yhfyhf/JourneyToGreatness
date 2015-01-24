class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        flag = True if n > 0 else False
        n = abs(n)
        res = 1
        while n >=2:
            tmp, i = x, 1
            while i*2 <= n:
                tmp *= tmp
                i *= 2
            n -= i
            res *= tmp
        if n == 1:
            res *= x

        if not flag:
            return 1/res
        return res

    # more elegant code
    def pow2(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1/ self.pow2(x, -n)
        elif n % 2:
            return self.pow2(x*x, n/2)*x
        else:
            return self.pow2(x*x, n/2)
            
if __name__ == '__main__':
    so = Solution()
    print so.pow(0.031, 44)

        