class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        for i in s:
            res = res*26 + (ord(i) - ord('A') + 1)
        return res

if __name__ == '__main__':
    so = Solution()
    klist = ['AA', 'A']
    for k in klist:
        print so.titleToNumber(k)