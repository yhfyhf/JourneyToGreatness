class Solution:
    # @return a string
    def intToRoman(self, num):
        # What I learned: instead of thinking 4, 9 logical, add them to data
        ROM = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL','X', 'IX', 'V', 'IV', 'I']
        INT = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ''
        for i in range(len(INT)):
            while num >= INT[i]:
                ans += ROM[i]
                num -= INT[i]
        return ans

    

if __name__ == '__main__':
    so = Solution()
    print so.intToRoman(2020)
