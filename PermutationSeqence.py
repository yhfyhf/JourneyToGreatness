import math
class Solution:
    # @return a string
    
    def getPermutation(self, n, k):
        """
        the number of permutation n is n!, which is n*(n-1)!.
        So the permutation is divided in n groups, we can know k
        is in which group by k/factorial(n-1), answer is the number
        of groups we can passed, but what if k is the last number of
        the group? so, we use k-1 instead. Now, do it recursively to
        get the kth permutation.
        
        """
        res = []
        def getKth(num, k):
            n = len(num)
            if n == 0:
                return 
            if k > math.factorial(n-1):
                groups = (k-1) / math.factorial(n-1)
                res.append(num[groups])
                num = num[:groups] + num[groups+1:]
                k -= groups * math.factorial(n-1)
            else:
                res.append(num[0])
                num = num[1:]
            getKth(num, k)

        getKth([str(x) for x in xrange(1, n+1)], k)
        return ''.join(res)
            
    
    def getPermutation_TLE1(self, n, k):
        """
        pruning to kth element
        """
        res = []
        if k > math.factorial(n):
            raise 'k is too big'
        self.cnt = 0
        def dfs(num, buf):
            if not num:
                res.append(buf)
                self.cnt += 1
                return
            if self.cnt >= k:
                return
            for i in xrange(len(num)):
                dfs(num[:i]+num[i+1:], buf+[num[i]])

        dfs([str(x) for x in xrange(1, n+1)], [])
        return ''.join(res[-1])



    def getPermutation_TLE2(self, n, k):
        # use generater to save memory, but TLE
        res = []
        if k > math.factorial(n):
            raise 'k is too big'

        def dfs(num, buf):
            if not num:
                yield buf
            for i in xrange(len(num)):
                for k in dfs(num[:i]+num[i+1:], buf+[num[i]]):
                    yield k

        res_gen = dfs([str(x) for x in xrange(1, n+1)], [])
        for i in xrange(k-1):
            next(res_gen)
        return next(res_gen)



if __name__ == '__main__':
    so = Solution()
    print so.getPermutation(3, 4)
