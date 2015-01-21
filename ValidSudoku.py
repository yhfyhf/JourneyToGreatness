
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # Horizontal
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                # number
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])

        # Vertical

        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in s:
                    return False
                else:
                    s.add(board[j][i])
        # 3x3 Cell
            
        for i in range(0,9,3):
            for j in range(0,9,3):
                s = set()
                for ii in range(3):
                    for jj in range(3):
                        if board[i+ii][j+jj] != '.':
                            print board[i+ii][j+jj], s
                        if board[i+ii][j+jj] == '.':
                            continue
                        if board[i+ii][j+jj] in s:
                            return False
                        else:
                            s.add(board[i+ii][j+jj])

        return True


    def isValidSudoku2(self, board):
        rows = [[False]*9 for i in range(9)]
        cols = [[False]*9 for i in range(9)]
        blocks = [[False]*9 for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                    c = int(board[i][j]) - 1
                    if rows[i][c] or cols[j][c] or blocks[3 * (i/3) + j/3][c]:
                        return False
                    else: # mark current, keep enumerating
                        rows[i][c] = cols[j][c] = blocks[3 * (i/3) + j/3][c] = True
                        
        return True
if __name__ == '__main__':
    so = Solution()
    board = ["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."]
    print so.isValidSudoku2(board)