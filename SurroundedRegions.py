import collections

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    
    def solve(self, board):
        if not board:
            return
        for l in xrange(len(board)):
            board[l] = list(board[l])
                #DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
        W, H = len(board[0]), len(board)
        queue = collections.deque()

        def fill(x,y):
            if x >= H or x < 0 or y >= W or y < 0 or board[x][y] != 'O':
                return
            board[x][y] = 'U'
            queue.append((x,y))
        
        def bfs(x, y):
            if board[x][y] == 'O':
                board[x][y] = 'U'
                queue.append((x,y))
            else:
                return
            # queue = collections.deque((x,y)) This will not insert as tuple
            while queue:
                e = queue.popleft()
                fill(e[0]-1, e[1])
                fill(e[0], e[1]+1)
                fill(e[0]+1, e[1])
                fill(e[0],e[1]-1)
                            
        for i in xrange(H):
            bfs(i, 0); bfs(i, W-1)
        for j in xrange(W):
            bfs(0, j); bfs(H-1, j)
        for i in xrange(H):
            for j in xrange(W):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    board[i][j] = 'O'
        

if __name__ == '__main__':
    mat = ["XOOOOOOOOOOOOOOOOOOO","OXOOOOXOOOOOOOOOOOXX","OOOOOOOOXOOOOOOOOOOX","OOXOOOOOOOOOOOOOOOXO","OOOOOXOOOOXOOOOOXOOX","XOOOXOOOOOXOXOXOXOXO","OOOOXOOXOOOOOXOOXOOO","XOOOXXXOXOOOOXXOXOOO","OOOOOXXXXOOOOXOOXOOO","XOOOOXOOOOOOXXOOXOOX","OOOOOOOOOOXOOXOOOXOX","OOOOXOXOOXXOOOOOXOOO","XXOOOOOXOOOOOOOOOOOO","OXOXOOOXOXOOOXOXOXOO","OOXOOOOOOOXOOOOOXOXO","XXOOOOOOOOXOXXOOOXOO","OOXOOOOOOOXOOXOXOXOO","OOOXOOOOOXXXOOXOOOXO","OOOOOOOOOOOOOOOOOOOO","XOOOOXOOOXXOOXOXOXOO"]

    so = Solution()
    so.solve(mat)
    print mat