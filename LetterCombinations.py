class Solution:
    # @return a list of strings, [s1, s2]

    def letterCombinations(self, digits):
        tab = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        self.dfs(tab, digits, res, "")
        return res

    def dfs(self, tab, digits, res, buff):
        """
        Args:
        tab: convert table
        digits: input string
        res: result list
        buff: buffer to store intermediate string
        cnt: buff length count
        """
        if len(digits) == 0:
            res.append(buff)
            return

        for c in tab[digits[0]]:
            self.dfs(tab, digits[1:], res, buff+c)
            

        
if __name__ == '__main__':
    so = Solution()
    print so.letterCombinations("23")