from random import randint
class Solution:
    # @param num, a list of integer
    # @return an integer
    # http://bookshadow.com/weblog/2014/12/14/leetcode-maximum-gap/
    # tried bitset, too slow, radix sort thought is right, but it need compression, just maintain min, max is enough
    
    def maximumGap(self, num):
        n = len(num)
        if n < 2:
            return 0
        A, B = min(num), max(num)
        # math.ceil((B-A)/(n-1))
        buc_range = max(1, (B - A - 1) / (n-1) + 1)
        buc_len = (B - A) / buc_range + 1
        buckets = [None for x in xrange(buc_len)]
        for i in num:
            loc = (i - A) / buc_range
            buc = buckets[loc]
            if buc is None:
                buc = {'min': i, 'max': i}
                buckets[loc] = buc
            else:
                buc['min'] = min(buc['min'], i)
                buc['max'] = max(buc['max'], i)
        res = 0
        while i < buc_len:
            if buckets[i] is None:
                continue
            j = i + 1
            while j < buc_len and buckets[j] is None:
                j += 1
            if j < buc_len:
                res = max(res, buckets[j]['min'] - buckets[i]['max'])
            i = j
        return res

if __name__ == '__main__':
    num = [x for x in xrange(999999)]
    num.append(88888890)
    so = Solution()
    print so.maximumGap(num)
        