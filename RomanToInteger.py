class Solution:
    # @param s, a string
    # @return an integer
    def romanToInt(self, s):
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            if i and table[s[i]] > table[s[i-1]]:
                res += table[s[i]] - 2 * table[s[i-1]]
            else:
                res += table[s[i]]
        return res
