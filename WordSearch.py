class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not board or not word:
            return False
        for i in xrange(len(board)):
            board[i] = list(board[i])
        h, w = len(board), len(board[0])
        res = False
        def testValid(xx, yy):
            if xx < 0 or xx > h-1 or yy < 0 or yy > w-1:
                return False
            return True
            
        def dfs(x, y, w):
            if len(w) == 0:
                return True
            DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i, j in DIR:
                if testValid(x+i, y+j) and board[x+i][y+j] == w[0]:
                    tmp, board[x][y] = board[x][y], '#'
                    if dfs(x+i, y+j, w[1:]):
                        return True
                    board[x][y] = tmp
            
        for i in xrange(h):
            for j in xrange(w):
                if board[i][j] == word[0]:
                    if dfs(i,j,word[1:]):
                        return True
        return False

if __name__ == '__main__':
    so = Solution()
    bd = [
        "ABCE",
        "SFCS",
        "ADEE"
    ]
 
    w1 = "ABCCED"
    w2 = "SEE"
    w3 = "ABCB"

    bd2 = [
        "CAA",
        "AAA",
        "BCD"
    ]
    w4 = "AAB"
    print so.exist(bd2, w4)
        