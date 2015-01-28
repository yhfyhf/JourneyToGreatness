class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        fives = 0
        while n/5:
            fives += n/5
            n /= 5
        return fives

if __name__ == '__main__':
    so = Solution()
    print so.trailingZeroes(15)