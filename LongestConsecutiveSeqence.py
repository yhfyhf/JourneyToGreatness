class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if not num:
            return 0
        num_set = set(num)
        low, high = 0, 0
        res = 1
        while num_set:
            e = num_set.pop()
            low, high = e, e
            while low-1 in num_set:
                low -= 1
                num_set.remove(low)
            while high+1 in num_set:
                high += 1
                num_set.remove(high)
            res = max((high-low+1), res)
        return res

if __name__ == '__main__':
    so = Solution()
    print so.longestConsecutive([])

        