class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.res = 0
        def check(x, y):
            for i in xrange(x):
                if board[i] == y or abs(x-i) == abs(board[i]-y):
                    return False
            return True

        def dfs(dep):
            if dep == n:
                self.res += 1
                return
            for col in xrange(n):
                if check(dep, col):
                    board[dep] = col
                    dfs(dep+1)
        board = [-1 for x in xrange(n)]
        dfs(0)
        return self.res

if __name__ == '__main__':
    so = Solution()
    print so.totalNQueens(8)