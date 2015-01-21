class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        # When n is too large, it might cause recursion depth exceeded
        if n == 0:
            return ''
        res = []
        self.dfs(n, 0, '', res)
        return res

    def dfs(self, left, right, buf, res):
        if left == 0:
            buf += right*')'
            res.append(buf)
            return
        else:
            self.dfs(left-1, right+1, buf+'(', res)
            if right > 0:
                self.dfs(left, right-1, buf+')', res)

if __name__ == '__main__':
    so = Solution()
    print so.generateParenthesis(3)