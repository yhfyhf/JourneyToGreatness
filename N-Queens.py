class Solution:
    # @return a list of lists of string

    def solveNQueens(self, n):
        res = []

        def check(x, y):
            for i in xrange(x):
                if board[i] == y or abs(x-i) == abs(board[i]-y):
                    return False
            return True
        
        def dfs(dep, buf):
            print dep, board
            if len(buf) == n:
                res.append(buf)
                return
            for col in xrange(n):
                if check(dep, col):
                    board[dep] = col
                    cur = '.'*n
                    dfs(dep+1, buf+[cur[:col]+'Q'+cur[col+1:]])
        board = [-1 for x in xrange(n)]
        dfs(0, [])
        return res

if __name__ == '__main__':
    so = Solution()
    res = so.solveNQueens(7)
    for b in res:
        for l in b:
            print l
        print '--------------------'
