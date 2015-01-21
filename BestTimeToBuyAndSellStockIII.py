
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        t1 = [0 for x in xrange(n)]
        t2 = [0 for x in xrange(n)]
        if not n:
            return 0
        low = prices[0]
        for i in xrange(1, n):
            low = min(low, prices[i])
            t1[i] = max(t1[i-1], prices[i]-low)

        high = prices[n-1]
        for i in xrange(n-2, -1, -1):
            high = max(high, prices[i])
            t2[i] = max(t2[i+1], high-prices[i])

        res = 0
        for i in xrange(n):
            if t1[i]+t2[i] > res:
                res = t1[i] + t2[i]
        return res


