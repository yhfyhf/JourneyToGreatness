class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        # Use dfs, backtracking
        # problem, string in Python is immutuable
        # based on x-zh's code
        dots = [(i,j) for i in range(9) for j in range(9) if board[i][j] == '.']

        # Be careful, dont use list comprehension, otherwise is not in-place modify
        # id(board) will change
        #board = [list(board[i]) for i in range(9)]
        for i in xrange(9):
            board[i] = list(board[i])
   
        
        def dfs(board, dots):
            if len(dots) == 0:
                return [''.join(line) for line in board]
                
            i, j = dots[0]
            for k in xrange(1, 10):
                c = str(k) # c is current guess
                # row, col, block check
                if c  not in board[i] \
                   and c not in [board[x][j] for x in xrange(9)] \
                   and c not in board[3*(i/3)][3*(j/3):3*(j/3)+3] \
                   and c not in board[3*(i/3) + 1][3*(j/3):3*(j/3)+3] \
                   and c not in board[3*(i/3) + 2][3*(j/3):3*(j/3)+3]:

                    
                    board[i][j] = c
                    #board[i] = ''.join(board[i][0:j]) + c + ''.join(board[i][j+1:])

                    res = dfs(board, dots[1:])
                    if res:
                        return res
                    board[i][j] = '.' # backtrack
                    #board[i] = ''.join(board[i][0:j]) + '.' + ''.join(board[i][j+1:])
            
            return False
            
        return dfs(board, dots)


            


if __name__ == '__main__':
    board = ["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."]
    board1 = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
    so = Solution()
    #print id(board1)
    print so.solveSudoku(board1)



    
