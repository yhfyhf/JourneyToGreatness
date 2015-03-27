// https://oj.leetcode.com/problems/sudoku-solver/

// Write a program to solve a Sudoku puzzle by filling the empty cells.
// Empty cells are indicated by the character '.'.
// You may assume that there will be only one unique solution.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
    bool valid(int x, int y, const vector<vector<char> > &board) {
	// col & row
	for (int i = 0; i < 9; i++) {
	    if (i != x && board[i][y] == board[x][y])
		return false;
	    if (i != y && board[x][i] == board[x][y])
		return false;
	}
	// 3*3
	for (int i = 3 * (x / 3); i < 3 * (x / 3 + 1); i++)
	    for (int j = 3 * (y / 3); j < 3 *(y / 3 + 1); j++)
		if ( (x != i || y != j) && board[x][y] == board[i][j]) 
		    return false;
	return true;
    }

    bool dfs(int row, int col, vector<vector<char> > &board) {
	if (row == 9)
	    return true;
	int nextrow = col == 8 ? row + 1 : row;
	int nextcol = col == 8 ? 0 : col + 1;
	if (board[row][col] != '.')
	    return dfs(nextrow, nextcol, board);
	for (char c = '1'; c <= '9'; c++) {
	    board[row][col] = c;
	    if (valid(row, col, board) && dfs(nextrow, nextcol, board))
		return true;
	    board[row][col] = '.';
	}
	return false;
    };
public:
    void solveSudoku(vector<vector<char> > &board) {
	dfs(0, 0, board);
    }
};

void p(const vector<vector<char> > &board) {
    for (auto l: board) {
	for (auto i: l)
	    cout<< i << " ";
	cout<<endl;
    }  
}

int main(int argc, char *argv[])
{
    Solution so;
    vector<vector<char> > board(9, vector<char>(9));
    string a[9] = {"..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",
		    ".98...3..","...8.3.2.","........6","...2759.."};
    for (int i = 0; i < 9; i++)
	for (int j = 0; j < 9; j++)
	    board[i][j] = a[i][j];
    so.solveSudoku(board);
    for (auto l: board) {
	for (auto k: l)
	    cout << k << " ";
	cout<<endl;
    }
	
    return 0;
}
